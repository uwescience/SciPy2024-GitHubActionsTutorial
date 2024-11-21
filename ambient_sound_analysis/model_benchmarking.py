# importing general Python libraries
import pandas as pd
import datetime as dt
import os
import matplotlib.pyplot as plt
import pytz
import plotly.graph_objects as go
import numpy as np

# importing orcasound_noise libraries
from orcasound_noise.pipeline.pipeline import NoiseAnalysisPipeline
from orcasound_noise.utils import Hydrophone
from orcasound_noise.pipeline.acoustic_util import plot_spec, plot_bb


# Set Location and Resolution
# Port Townsend, 1 Hz Frequency, 60-second samples
if __name__ == '__main__':
    pipeline = NoiseAnalysisPipeline(Hydrophone.ORCASOUND_LAB,
                                     delta_f=10, bands=None,
                                     delta_t=60, mode='safe')




# Generate parquet dataframes with noise levels for a time period

# now = dt.datetime.now(pytz.timezone('US/Pacific'))
# fix time
now = dt.datetime(2024, 6, 1, 17, 0, 0)
psd_path, broadband_path = pipeline.generate_parquet_file(now - dt.timedelta(hours = 13), 
                                                          now - dt.timedelta(hours = 8), 
                                                          upload_to_s3=False)

# Read the parquet files
# psd_df = pd.read_parquet(psd_path)
bb_df = pd.read_parquet(broadband_path)

# set threshold
threshold = 4

import numpy as np
nof_ships = (np.diff((bb_df['0']>threshold).astype('uint8'))==1).sum()


# Create a new directory if it does not exist
if not os.path.exists('ambient_sound_analysis/csv'):
   os.makedirs('ambient_sound_analysis/csv')

# pd.DataFrame([nof_ships]).to_csv('ambient_sound_analysis/csv/'+str(now)+'.csv', header=False, index=False)

print("Nof Ships: "+str(nof_ships))
pd.DataFrame([nof_ships]).to_csv('ambient_sound_analysis/csv/test.csv', header=False, index=False)






# Create and save psd plot 
# fig = plot_spec(psd_df)
# fig.write_image('ambient_sound_analysis/img/psd.png')

# Create and save bb plot
# fig = plot_bb(bb_df)
# fig.savefig('ambient_sound_analysis/img/broadband.png')
