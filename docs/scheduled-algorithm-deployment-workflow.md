# Scheduled Algorithm Deployment Workflow

## Use Case: Orcasound Stream Spectrogram Visualization

Next, we will demonstrate how GitHub Actions can be used to display a spectrogram for a segment from an underwater audio stream.

Spectrogram Visualization Workflow: [`.github/workflows/noise_processing.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/noise_processing.yml)

Workflow Steps:

* Generate spectrogram for a period of time (with `ambient_sound_analysis` package)
	* Download data from AWS S3 bucket (in `.ts` format) for a given time period
	* Convert many small `.ts` files to one file in `.wav` format
  	* Generate power spectrogram and store it in `.parquet` format
* Read the power spectrogram in `pandas` dataframe format 
* Create plots and save them: `psd.png` and `broadband.png`.
* Upload the `.png` files to GitHub 

After the workflow is executed `psd.png` and `broadband.png`files are updated in the repo and are visualized below.
![alt text](https://raw.githubusercontent.com/uwescience/SciPy2024-GitHubActionsTutorial/main/ambient_sound_analysis/img/psd.png)

![alt text](https://raw.githubusercontent.com/uwescience/SciPy2024-GitHubActionsTutorial/main/ambient_sound_analysis/img/broadband.png)