# Collaborative Model Versioning and Benchmarking

Here we will describe a scenario in which users submit different models to be applied to common data and compare the results. For this we will leverage GitHub's core features to facilitate code versioning and collaborative development and will set up a GitHub Actions configuration which triggers the evaluation when a user creates a `pull request` with a new version of the model and updates a table with user's results and corresponding commit number.

We will use a simple approach to approximate the number of ships passing during a time window by counting the number of peaks that appear above a threshold in the broadband plot. The threshold is set in the [`model_benchmarking.py`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/ambient_sound_analysis/model_benchmarking.py) script.


## Model Versioning Workflow
The workflow which triggers the model evaluation is in [`model_benchmarking.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/model_benchmarking.yml). It consists of the following steps:

1. it gets triggered on 	`pull_request` 
	* `synchronize` type ensures it get triggered when somebody updates existing pull request
2. it runs the `model_benchmarking.py` script which creates a `.csv` file containing the estimated number of ships
3. It appends to the row with number of ships extra metatada of the submission: username, commit SHA, pull request title
4. It stores the row to a `score_[SHA].csv`
5. It commits the 1-row file to the `ambient_sound_analysis/csv` folder


## Model Benchmarking Workflow

The next workflow follows the steps `create_website_spectrogram` workflow, which converts a notebook [`display_benchmarks`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/ambient_sound_analysis/display_benchmarks.ipynb) to a website. In this case, we have a very simple notebook which reads all `score_[SHA].csv` and displays a "benchmark table" with the individual entries. This notebook is converted to a webpage ([https://uwescience.github.io/SciPy2024-GitHubActionsTutorial/display_benchmarks.html](https://uwescience.github.io/SciPy2024-GitHubActionsTutorial/display_benchmarks.html/)).











 