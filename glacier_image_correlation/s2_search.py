import xarray as xr
import os
import pystac
import pystac_client
import stackstac
from dask.distributed import Client
import dask
import json
import pandas as pd
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="Search for Sentinel-2 images")
    parser.add_argument("cloud_cover", type=str, help="percent cloud cover allowed in images (0-100)")
    parser.add_argument("start_month", type=str, help="first month of year to search for images")
    parser.add_argument("stop_month", type=str, help="last month of year to search for images")
    parser.add_argument("npairs", type=str, help="number of pairs per image")
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    
    # hardcode bbox for now
    bbox = {
        "type": "Polygon",
        "coordinates": [
            [[75.42382800808971,36.41082887114753],
             [75.19442677164156,36.41082887114753],
             [75.19442677164156,36.201076360872946],
             [75.42382800808971,36.201076360872946],
             [75.42382800808971,36.41082887114753]]]
    }
    
    # Use the api from element84 to query the data
    URL = "https://earth-search.aws.element84.com/v1"
    catalog = pystac_client.Client.open(URL)
    
    search = catalog.search(
        collections=["sentinel-2-l2a"],
        intersects=bbox,
        query={"eo:cloud_cover": {"lt": float(args.cloud_cover)}}
    )
    
    # Check how many items were returned
    items = search.item_collection()
    print(f"Returned {len(items)} Items")
    
    # create xarray dataset without loading data
    sentinel2_stack = stackstac.stack(items)
    # filter to specified month range
    sentinel2_stack_snowoff = sentinel2_stack.where((sentinel2_stack.time.dt.month >= int(args.start_month)) & (sentinel2_stack.time.dt.month <= int(args.stop_month)), drop=True)
    
    # select first image of each month
    period_index = pd.PeriodIndex(sentinel2_stack_snowoff['time'].values, freq='M')
    sentinel2_stack_snowoff.coords['year_month'] = ('time', period_index)
    first_image_indices = sentinel2_stack_snowoff.groupby('year_month').apply(lambda x: x.isel(time=0))
    
    product_names = first_image_indices['s2:product_uri'].values.tolist()
    print('\n'.join(product_names))
    
    # Create Matrix Job Mapping (JSON Array)
    pairs = []
    for r in range(len(product_names) - int(args.npairs)):
        for s in range(1, int(args.npairs) + 1 ):
            img1_product_name = product_names[r]
            img2_product_name = product_names[r+s]
            shortname = f'{img1_product_name[11:19]}_{img2_product_name[11:19]}'
            pairs.append({'img1_product_name': img1_product_name, 'img2_product_name': img2_product_name, 'name':shortname})
    matrixJSON = f'{{"include":{json.dumps(pairs)}}}'
    print(f'number of image pairs: {len(pairs)}')
    
    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        print(f'IMAGE_DATES={product_names}', file=f)
        print(f'MATRIX_PARAMS_COMBINATIONS={matrixJSON}', file=f)

if __name__ == "__main__":
   main()
