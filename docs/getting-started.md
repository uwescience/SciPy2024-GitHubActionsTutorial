# Setup

* We expect all participants to have a GitHub account (if not you can make one here [https://github.com/login](https://github.com/login))
* Fork [https://github.com/uwescience/SciPy2024-GitHubActionsTutorial](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial)
* Enable GitHub Actions:
  * Settings ->   Actions -> Allow actions and reusable workflows
  * [Managing Permissions 
Documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository)


All workflow configurations are stored in the [`.github/workflows`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/tree/main/.github/workflows) folder and we will go through them in the following order:

1. [`python_env.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/python_env.yml)
2. [`conda_env.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/conda_env.yml)
3. [`noise_processing.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/noise_processing.yml)
4. [`create_website_spectrogram.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/create_website_spectrogram.yml)
5. [`create_website.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/create_website.yml)
6. [`batch_image_correlation.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/batch_image_correlation.yml)
7. [`image_correlation_pair.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/image_correlation_pair.yml)
8. [`summary_statistics.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/summary_statistics.yml)
9. [`model_benchmarking.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/model_benchmarking.yml)
10. [`create_website_benchmarks`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/create_website_benchmarks.yml)

 






























