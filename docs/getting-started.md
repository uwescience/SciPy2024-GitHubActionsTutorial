# Setup
* Fork this repo
* Enable Github Actions:
  * Settings ->   Actions -> Allow actions and reusable workflows
  * [Managing Permissions 
Documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository)


All workflow configurations are stored in the [`.github/workflows`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/tree/main/.github/workflows) and will go through them in the following order:

1. [`python_env.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/python_env.yml)
2. [`conda_env.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/conda_env.yml)
3. [`noise_processing.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/noise_processing.yml)
4. [`create_website_spectrogram.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/create_website_spectrogram.yml)
5. [`create_website.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/create_website.yml)
6. ...

 






























