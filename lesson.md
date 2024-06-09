# Setup 
* Fork this repo
* Enable Github Actions:
  * Settings ->   Actions -> Allow actions and reusable workflows
  * [Managing Permissions Documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#managing-github-actions-permissions-for-your-repository) 

# GitHub Actions Python Environment Workflow
First, we will run a basic workflow which creates a python environment with a few scientific packages and prints out their version
* [.github/workflows/python_env.yml](https://github.com/valentina-s/GithubActionsTutorial-USRSE23/blob/main/.github/workflows/python_env.yml)
* go to **Actions** tab, click on **Python Environment**, and click **Run workflow**: this will manually trigger the workflow ([`dispatch_workflow`](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow))
* click on the newly created run to see the execution progress

# Orcasound Spectrogram Visualization Workflow

Next, we will demonstrate how GitHub Actions can be used to display a spectrogram of a snippet from an underwater audio stream.

* [`.github/workflows/orcasound_processing.yml`](https://github.com/valentina-s/GithubActionsTutorial-USRSE23/blob/main/.github/workflows/orcasound_processing.yml)
* workflow steps:
  * download data from S3 for a particular timestamp
  * convert the last file from `.ts` to `.wav` format (in [`orcasound_processing.py`](https://github.com/valentina-s/GithubActionsTutorial-USRSE23/blob/main/orcasound_processing.py))
  * create and save spectrogram in `spec.png` (in [`orcasound_processing.py`](https://github.com/valentina-s/GithubActionsTutorial-USRSE23/blob/main/orcasound_processing.py))
  * upload `spec.png` to GitHub 

After the workflow is executed a `spec.png` file is updated in the repo and is visualized below.
![alt text](https://raw.githubusercontent.com/valentina-s/orca-action-workflow-test/main/png/spec.png)
