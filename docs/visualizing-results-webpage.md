
# Visualizing Results on a Webpage

We saw it is pretty easy to continuously update results on the Readme of the repository. However, sometimes we would like to display them on a website. 



We will demonstrate the scenario of converting a Jupyter Notebook to a webpage. 

Notebook: [`plot_noise_levels.ipynb`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/ambient_sound_analysis/plot_noise_levels.ipynb)

Create Website with Spectrogram Workflow: [`.github/workflows/create_website_spectrogram.yml`](https://github.com/uwescience/SciPy2024-GitHubActionsTutorial/blob/main/.github/workflows/create_website_spectrogram.yml)


The process consists of the following stages:

* build the website:
  * use `nbconvert` to convert the notebook to an html webpage
    * `jupyter nbconvert plot_noise_levels.ipynb --execute --to html --output-dir=_build/html --no-input` 	
    * upload the built content as an artifact using the `upload-pages-artifact` action

* deploy the website (if built successfully):
  * configure website with `actions/configure-pages`
  * deploy website with `actions/deploy-pages`

The website can be found here:

[https://uwescience.github.io/SciPy2024-GitHubActionsTutorial/plot\_noise\_levels.html](https://uwescience.github.io/SciPy2024-GitHubActionsTutorial/plot_noise_levels.html)  


The procedure is set up to run on `push` thus every time the notebook is updated the website is updated. 

The plots in the notebook use `plotly` and they have interactive features. Those are preserved in the website providing the ability to engage with the data without having to run a notebook.

The notebook does not display any code which is conventient for showing results to the public. This was achieved by providing the `--no-input` argument to `nbconvert`. We also set the `%capture` magic in the notebook to capture some subprocess output. One can configure this further using cell tags to display content selectively.





Other ways: 

* [Jupyterbook](https://jupyterbook.org/en/stable/publish/gh-pages.html)
* [Readthedocs](https://about.readthedocs.com/?ref=readthedocs.com)
* Jekyll template 
* Dashboard