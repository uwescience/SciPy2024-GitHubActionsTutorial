# Overview

1. [Setup](#setup)
2. [GitHub Actions Python Environment](#github-actions-python-environment-workflow)
3. [Orcasound Spectrogram Visualization Workflow](#orcasound-spectrogram-visualization-workflow)
4. [Exporting Results](#exporting-results)
5. [Scaling Workflows](#scaling-workflows)

# Setup 
* Fork this repo
* Enable Github Actions:
  * Settings ->   Actions -> Allow actions and reusable workflows
  * [Managing Permissions Documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#managing-github-actions-permissions-for-your-repository) 

# GitHub Actions Python Environment Workflow

## Installing Packages with `pip`
First, we will run a basic workflow which creates a python environment with a few scientific packages and prints out their version.

Python Environment Workflow Configuration:
[`.github/workflows/python_env.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/python_env.yml)


* Go to **Actions** tab
* Click on **Python Environment**
* Click **Run workflow**: this will manually trigger the workflow ([`dispatch_workflow`](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow))
* Click on the newly created run to see the execution progress


### Exercise: 
Edit [`.github/workflows/python_env.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/python_env.yml) to install packages popular in your research. Trigger the workflow to monitor their installation.


## Installing Packages with Conda
We can also install packages through conda (instead of `pip`). We will use a `miniconda-setup` action to achieve that easily.


Conda Environment Workflow Configuration [`.github/workflows/conda_env.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/conda_env.yml)

# Orcasound Spectrogram Visualization Workflow

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


# Exporting Results

We will discuss several different ways to export results.

## Uploading to the GitHub Repository

One of the easiest ways to display results is to store them in the GitHub repository. This can be a quick solution, for example, to display a small plot or a table within the `Readme.md` of the repository and update it as the workflow is rerun. This is not a practical solution for big outputs as the GitHub repositories are recommended to not exceed more than 1GB, and all versions of the files will be preserved in the repository's history (thus slowing down cloning). 

It is possible to execute all steps to add, commit, and push a file to GitHub, but there is already an [GitHub Auto Commit Action]https://github.com/marketplace/actions/git-auto-commit) to achieve that.

![alt text](https://raw.githubusercontent.com/uwescience/SciPy2024-GitHubActionsTutorial/main/img/auto-commit-action.png)


## Uploading as a GitHub Workflow Artifact

GitHub provides an option for temporary storage of GitHub Action data as Workflow Artifacts. These are kept on the GitHub website as zipped files and can downloaded within 90 days for public repositories, or 400 days for private repositories.

There is a GitHub Action which can upload file/s as GitHub Artifacts. 

![alt text](https://raw.githubusercontent.com/uwescience/SciPy2024-GitHubActionsTutorial/main/img/artifact-upload-action.png)

The artifact can be found by clicking on the workflow run and scrolling down to a section Artifacts.

![alt text](https://raw.githubusercontent.com/uwescience/SciPy2024-GitHubActionsTutorial/main/img/artifact_github_interface.png)


The artifact can be downloaded directly from the interface but also can be downloaded through the GitHub client.

```
gh run download
```

The workflow run also provides a publicly available link to the download artifact:

Artifact download URL: [https://github.com/uwescience/SciPy2024-
GitHubActionsTutorial/actions/runs/9591972369/artifacts/1619380017](https://github.com/uwescience/SciPy2024-
GitHubActionsTutorial/actions/runs/9591972369/artifacts/1619380017)

There is a `download-artifact` action to download the artifacts and share between jobs within a workflow run (note this is limited to the inidividual workflow run, for downloading across runs use the other options).

[Here](Artifact download URL: https://github.com/uwescience/SciPy2024-
GitHubActionsTutorial/actions/runs/9591972369/artifacts/1619380017) is more detailed documentation on GitHub Artifacts.




## Uploading to Personal Storage

A more long-term solution is to store outputs to personal storage. This could be for example Google Drive or a Cloud Provider Object Storage such as an AWS S3 bucket. To have a write access to these storage systems one will need to provide the credential information securely to GitHub Actions. This can be achieved through storing the credential information as Action Secrets.

The write operation can be performed directly from the Python code or from the GitHub Action configuration. Here will demonstrate how to upload data to Google Drive with `rclone`, a tool for transferring data between storage system which is quite provide agnostic.

The approach consists of a few steps:

1. use an `rclone` GitHub Action to avoid installing `rclone` manually
  *  we will use [AnimMouse/setup-rclone](https://github.com/marketplace/actions/setup-rclone-action)
* configure a Google Drive remote locally
* encode the text in the config file and save it as a secret `RCLONE_CONFIG`
  * MacOX: `openssl base64 -in ~/.config/rclone/rclone_drive.conf`
* run the `rclone` command to upload the plots to Google Drive
  *  `rclone copy ambient_sound_analysis/img/broadband.png mydrive:rclone_uploads/`

  
 ![alt txt](https://raw.githubusercontent.com/uwescience/SciPy2024-GitHubActionsTutorial/main/img/rclone_upload.png)
 
[Secrets Documentation](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)




# Visualizing Results on a Webpage

# Scaling Workflows
























