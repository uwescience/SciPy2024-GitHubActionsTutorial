# importing general Python libraries
import pandas as pd
import datetime as dt
import os
import matplotlib.pyplot as plt
import pytz
import plotly.graph_objects as go

# importing orcasound_noise libraries
from orcasound_noise.pipeline.pipeline import NoiseAnalysisPipeline
from orcasound_noise.utils import Hydrophone
from orcasound_noise.pipeline.acoustic_util import plot_spec, plot_bb


# Set Location and Resolution
# Port Townsend, 1 Hz Frequency, 60-second samples
if __name__ == '__main__':
    pipeline = NoiseAnalysisPipeline(Hydrophone.PORT_TOWNSEND,
                                     delta_f=10, bands=None,
                                     delta_t=60, mode='safe')




# Generate parquet dataframes with noise levels for a time period

now = dt.datetime.now(pytz.timezone('US/Pacific'))
psd_path, broadband_path = pipeline.generate_parquet_file(now - dt.timedelta(hours = 9), 
                                                          now - dt.timedelta(hours = 8), 
                                                          upload_to_s3=False)

# Read the parquet files
psd_df = pd.read_parquet(psd_path)
bb_df = pd.read_parquet(broadband_path)

# Create a new directory if it does not exist
if not os.path.exists('ambient_sound_analysis/img'):
   os.makedirs('ambient_sound_analysis/img')

# Create and save psd plot 
fig = plot_spec(psd_df)
fig.write_image('ambient_sound_analysis/img/psd.png')

# Create and save bb plot
fig = plot_bb(bb_df)
fig.savefig('ambient_sound_analysis/img/broadband.png')
