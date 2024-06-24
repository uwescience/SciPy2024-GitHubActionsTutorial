# Caching 

Dependency reinstalls between consecutive workflow runs are time consuming, and usually unnecessary. The process can be sped up by caching the builds of the packages. Caches are removed automatically if not accessed for 7 days, and their size can be up to 10GB. One can also manually remove a cache, if they want to reset the installation.

## Caching `pip` installs

`pip` packages can be cached by adding the `cache: 'pip'` setting to the Python setup action. If one is not using the default `requirements.txt` file for installation, they should also provide a `dependency-path`.

![alt text](https://raw.githubusercontent.com/uwescience/SciPy2024-GitHubActionsTutorial/main/img/pip-caching.png)

## Caching `conda` installs

Conda packages can be similarly cached withing the conda setup action.

![alt text](https://raw.githubusercontent.com/uwescience/SciPy2024-GitHubActionsTutorial/main/img/conda-caching.png)

## Caching `apt-get` installs

Packages such as `ffmpeg` can take long time to install. There is no official action to cache apt-get packages but they can be cached with the [walsh128/cache-apt-pkgs-action](https://github.com/marketplace/actions/cache-apt-packages).

```yaml
- uses: walsh128/cache-apt-pkgs-action@latest
  with:
  packages: ffmpeg
```

## Caching any data

The general [`cache`](https://github.com/marketplace/actions/cache) action allows to cache data at any path. Apart from builds of packages, one can use this option to not regenerate results while testing.

```yaml
- uses: actions/cache@v4
  id: cache
  with:
    path: img/
    key: img

- name: Get all files
  if: steps.cache.outputs.cache-hit != 'true'
  run: …
```

[Caching Documentation](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows)

