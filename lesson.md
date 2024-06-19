# Setup 
* Fork this repo
* Enable Github Actions:
  * Settings ->   Actions -> Allow actions and reusable workflows
  * [Managing Permissions Documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#managing-github-actions-permissions-for-your-repository) 

# GitHub Actions Python Environment Workflow

First, we will run a basic workflow which creates a python environment with a few scientific packages and prints out their version
* [.github/workflows/python_env.yml](https://github.com/valentina-s/GithubActionsTutorial-USRSE23/blob/main/.github/workflows/python_env.yml(https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/python_env.yml))
* go to **Actions** tab, click on **Python Environment**, and click **Run workflow**: this will manually trigger the workflow ([`dispatch_workflow`](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow))
* click on the newly created run to see the execution progress

## Conda Environment
We can also install packages through conda (instead of `pip`). We will use a `miniconda-setup` action to achieve that easily.

[.github/workflows/conda_env.yml](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/conda_env.yml)

# Orcasound Spectrogram Visualization Workflow

Next, we will demonstrate how GitHub Actions can be used to display a spectrogram for a segment from an underwater audio stream.

* [`.github/workflows/noise_processing.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/noise_processing.yml)
* workflow steps:
  * generate spectrogram for a period of time (with `ambient_sound_analysis` package)
  		* Download data from AWS S3 bucket (in `.ts` format) for a given time period
  		* Convert many small `.ts` files to one file in `.wav` format
  		* Generate power spectrogram and store it in `.parquet` format
  * read the power spectrogram in `pandas` dataframe format 
  * create plots and save it as a `psd.png`.
  * upload `psd.png` to GitHub 

After the workflow is executed a `psd.png` and `broadband.png`files are updated in the repo and is visualized below.
![alt text](https://raw.githubusercontent.com/uwescience/SciPy2024-GitHubActionsTutorial/main/ambient_sound_analysis/img/psd.png)

![alt text](https://raw.githubusercontent.com/uwescience/SciPy2024-GitHubActionsTutorial/main/ambient_sound_analysis/img/broadband.png)




