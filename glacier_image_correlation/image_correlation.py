#! /usr/bin/env python

import xarray as xr
import rasterio as rio
import rioxarray
import numpy as np
import os
from autoRIFT import autoRIFT
from scipy.interpolate import interpn
import pystac
import pystac_client
import stackstac
from dask.distributed import Client
import geopandas as gpd
from shapely.geometry import shape
import dask
import warnings
import argparse

# silence some warnings from stackstac and autoRIFT
warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=UserWarning)

def download_s2(img1_product_name, img2_product_name, bbox):
    '''
    Download a pair of Sentinel-2 images acquired on given dates over a given bounding box
    '''
    # GDAL environment variables for better performance
    os.environ['AWS_REGION']='us-west-2'
    os.environ['GDAL_DISABLE_READDIR_ON_OPEN']='EMPTY_DIR' 
    os.environ['AWS_NO_SIGN_REQUEST']='YES' 

    # We use the api from element84 to query the data
    URL = "https://earth-search.aws.element84.com/v1"
    catalog = pystac_client.Client.open(URL)

    search = catalog.search(
    collections=["sentinel-2-l2a"],
    query=[f's2:product_uri={img1_product_uri}'])
    
    img1_items = search.item_collection()
    img1_full = stackstac.stack(img1_items)

    search = catalog.search(
    collections=["sentinel-2-l2a"],
    query=[f's2:product_uri={img2_product_uri}'])

    # Check how many items were returned
    img2_items = search.item_collection()
    img2_full = stackstac.stack(img2_items)

    aoi = gpd.GeoDataFrame({'geometry':[shape(bbox)]})
    # crop images to aoi
    img1_clipped = img1_full.rio.clip_box(*aoi.total_bounds,crs=4326) 
    img2_clipped = img2_full.rio.clip_box(*aoi.total_bounds,crs=4326)
    
    img1_ds = img1_clipped.to_dataset(dim='band')
    img2_ds = img2_clipped.to_dataset(dim='band')

    return img1_ds, img2_ds 

def run_autoRIFT(img1, img2, skip_x=3, skip_y=3, min_x_chip=16, max_x_chip=64,
                 preproc_filter_width=3, mpflag=4, search_limit_x=30, search_limit_y=30):
    '''
    Configure and run autoRIFT feature tracking with Sentinel-2 data for large mountain glaciers
    '''
        
    obj = autoRIFT()
    obj.MultiThread = mpflag

    obj.I1 = img1
    obj.I2 = img2

    obj.SkipSampleX = skip_x
    obj.SkipSampleY = skip_y

    # Kernel sizes to use for correlation
    obj.ChipSizeMinX = min_x_chip
    obj.ChipSizeMaxX = max_x_chip
    obj.ChipSize0X = min_x_chip
    # oversample ratio, balancing precision and performance for different chip sizes
    obj.OverSampleRatio = {obj.ChipSize0X:16, obj.ChipSize0X*2:32, obj.ChipSize0X*4:64}

    # generate grid
    m,n = obj.I1.shape
    xGrid = np.arange(obj.SkipSampleX+10,n-obj.SkipSampleX,obj.SkipSampleX)
    yGrid = np.arange(obj.SkipSampleY+10,m-obj.SkipSampleY,obj.SkipSampleY)
    nd = xGrid.__len__()
    md = yGrid.__len__()
    obj.xGrid = np.int32(np.dot(np.ones((md,1)),np.reshape(xGrid,(1,xGrid.__len__()))))
    obj.yGrid = np.int32(np.dot(np.reshape(yGrid,(yGrid.__len__(),1)),np.ones((1,nd))))
    noDataMask = np.invert(np.logical_and(obj.I1[:, xGrid-1][yGrid-1, ] > 0, obj.I2[:, xGrid-1][yGrid-1, ] > 0))

    # set search limits
    obj.SearchLimitX = np.full_like(obj.xGrid, search_limit_x)
    obj.SearchLimitY = np.full_like(obj.xGrid, search_limit_y)

    # set search limit and offsets in nodata areas
    obj.SearchLimitX = obj.SearchLimitX * np.logical_not(noDataMask)
    obj.SearchLimitY = obj.SearchLimitY * np.logical_not(noDataMask)
    obj.Dx0 = obj.Dx0 * np.logical_not(noDataMask)
    obj.Dy0 = obj.Dy0 * np.logical_not(noDataMask)
    obj.Dx0[noDataMask] = 0
    obj.Dy0[noDataMask] = 0
    obj.NoDataMask = noDataMask

    print("preprocessing images")
    obj.WallisFilterWidth = preproc_filter_width
    obj.preprocess_filt_lap() # preprocessing with laplacian filter
    obj.uniform_data_type()

    print("starting autoRIFT")
    obj.runAutorift()
    print("autoRIFT complete")

    # convert displacement to m
    obj.Dx_m = obj.Dx * 10
    obj.Dy_m = obj.Dy * 10
        
    return obj

def prep_outputs(obj, img1_ds, img2_ds):
    '''
    Interpolate pixel offsets to original dimensions, calculate total horizontal velocity
    '''

    # interpolate to original dimensions 
    x_coords = obj.xGrid[0, :]
    y_coords = obj.yGrid[:, 0]
    
    # Create a mesh grid for the img dimensions
    x_coords_new, y_coords_new = np.meshgrid(
        np.arange(obj.I2.shape[1]),
        np.arange(obj.I2.shape[0])
    )
    
    # Perform bilinear interpolation using scipy.interpolate.interpn
    Dx_full = interpn((y_coords, x_coords), obj.Dx, (y_coords_new, x_coords_new), method="linear", bounds_error=False)
    Dy_full = interpn((y_coords, x_coords), obj.Dy, (y_coords_new, x_coords_new), method="linear", bounds_error=False)
    Dx_m_full = interpn((y_coords, x_coords), obj.Dx_m, (y_coords_new, x_coords_new), method="linear", bounds_error=False)
    Dy_m_full = interpn((y_coords, x_coords), obj.Dy_m, (y_coords_new, x_coords_new), method="linear", bounds_error=False)
    
    # add variables to img1 dataset
    img1_ds = img1_ds.assign({'Dx':(['y', 'x'], Dx_full),
                              'Dy':(['y', 'x'], Dy_full),
                              'Dx_m':(['y', 'x'], Dx_m_full),
                              'Dy_m':(['y', 'x'], Dy_m_full)})
    # calculate x and y velocity
    img1_ds['veloc_x'] = (img1_ds.Dx_m/(img2_ds.time.isel(time=0) - img1_ds.time.isel(time=0)).dt.days)*365.25
    img1_ds['veloc_y'] = (img1_ds.Dy_m/(img2_ds.time.isel(time=0) - img1_ds.time.isel(time=0)).dt.days)*365.25
    
    # calculate total horizontal velocity
    img1_ds['veloc_horizontal'] = np.sqrt(img1_ds['veloc_x']**2 + img1_ds['veloc_y']**2)

    return img1_ds

def get_parser():
    parser = argparse.ArgumentParser(description="Run autoRIFT to find pixel offsets for two Sentinel-2 images")
    parser.add_argument("img1_product_name", type=str, help="product name of first Sentinel-2 image")
    parser.add_argument("img2_product_name", type=str, help="product name of first Sentinel-2 image")
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()

    # hardcoding a bbox for now
    bbox = {
    "type": "Polygon",
    "coordinates": [
          [
            [75.42382800808971,36.41082887114753],
            [75.19442677164156,36.41082887114753],
            [75.19442677164156,36.201076360872946],
            [75.42382800808971,36.201076360872946],
            [75.42382800808971,36.41082887114753]
          ]
        ],
    }

    # download Sentinel-2 images
    img1_ds, img2_ds = download_s2(args.img1_product_name, args.img2_product_name, bbox)
    # grab near infrared band only
    img1 = img1_ds.nir.squeeze().values
    img2 = img2_ds.nir.squeeze().values

    print(img2.shape)
    
    # scale search limit with temporal baseline assuming max velocity 1000 m/yr (100 px/yr)
    search_limit_x = search_limit_y = round(((((img2_ds.time.isel(time=0) - img1_ds.time.isel(time=0)).dt.days)*100)/365.25).item())
    
    # run autoRIFT feature tracking
    obj = run_autoRIFT(img1, img2, search_limit_x=search_limit_x, search_limit_y=search_limit_y)
    # postprocess offsets
    ds = prep_outputs(obj, img1_ds, img2_ds)

    # write out velocity to tif
    ds.veloc_horizontal.rio.to_raster(f'S2_{args.img1_date}_{args.img2_date}_horizontal_velocity.tif')

if __name__ == "__main__":
   main()
