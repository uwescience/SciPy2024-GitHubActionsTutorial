# Measuring Glacier Surface Velocity
#### Quinn Brencher, University of Washington

This set of Github Actions workflows allows you to measure horizontal glacier surface velocity from Sentinel-2 image pairs using [autoRIFT software](https://github.com/nasa-jpl/autoRIFT). No external accounts or API keys are required. These workflows were created for the Github Actions for Scientific Data Workflows workshop and the 2024 SciPy conference. 

## Usage
We use three workflows to make measurements of glacier surface velocity. For demonstration purposes the workflows are only set up to work over the [Yazghil Glacier](https://earth.google.com/earth/d/1myewNJrDEM0tW1_xdpWCYaRCGDcOBwiy?usp=drive_link) in Pakistan. To run the workflows, simply fork this repository, visit the "Actions" tab, and choose the `batch_image_correlation` workflow (which runs the other two workflows as well). 

### 1. `image_correlation_pair`
This workflow calls a Python script (image_correlation.py) that runs autoRIFT on a pair of spatially overlapping [Sentinel-2 L2A](https://docs.sentinel-hub.com/api/latest/data/sentinel-2-l2a/) images. It only requires the [product names](https://sentiwiki.copernicus.eu/web/s2-products) of the two images. The images are downloaded from aws using the [Element 84 Earth Search API](https://element84.com/earth-search/). Only the near infrared band (NIR, B08) is used which has a spatial resolution of 10 m. autoRIFT is used to perform image correlation. Search distances are scaled with temporal baseline assuming a maximum surface velocity of 1000 m/yr, so images acquired farther apart in time take longer to process. Surface velocity maps are saved as geotifs and uploaded as [Github Artifacts](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts). 

![plot](./images/input_images.png)

### 2. `batch_image_correlation`
This workflow can be used to create surface velocity maps from many pairs of Sentinel-2 images. Required inputs include maximum cloud cover percent, start month (recommend >=5 to minimize snow cover), end month (recommend <=10 to minimize snow cover), and number of pairs per image, e.g.:
- 1 pair per image: (img<sub>i</sub>, img<sub>i+1</sub>), (img<sub>i+1</sub>, img<sub>i+2</sub>), (img<sub>i+2</sub>, img<sub>i+3</sub>), ...
- 2 pairs per image: (img<sub>i</sub>, img<sub>i+1</sub>), (img<sub>i</sub>, img<sub>i+2</sub>), (img<sub>i+1</sub>, img<sub>i+2</sub>), ...
- 3 pairs per image: (img<sub>i</sub>, img<sub>i+1</sub>), (img<sub>i</sub>, img<sub>i+2</sub>), (img<sub>i</sub>, img<sub>i+3</sub>), ...

Only the first suitable image is selected for each month. Once image pairs are identified, a matrix job is set up to run `image_correlation_pair` for each pair. Finally, `summary_statistics` is run. 

### 3. `summary_statistics`
This workflow downloads all of the velocity maps created during a `batch_image_correlation` run and uses them to calculate and plot median velocity, standard deviation of velocity, and valid pixel count across all velocity maps. The summary statistics plot is uploaded as a Github Artifact.  

![plot](./images/velocity_summary_statistics.png)


## Acknowledgements
- Scott Henderson developed much of the original ideas and code used for this set of workflows
- [University of Washington eScience Incubator Program 2024](https://escience.washington.edu/incubator-24-glacial-lakes/)