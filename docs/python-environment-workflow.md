# Python Environment Workflow

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

