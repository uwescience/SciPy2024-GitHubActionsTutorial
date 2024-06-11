# Turn a Jupyter Notebook into a public website

The basic idea is to *execute* a notebook and render both code and figures on a website

(nbconvert)[https://nbconvert.readthedocs.io] is a tool in the Jupyter ecosystem to convert .ipynb to various formats including HTML

We'll run this command
`jupyter nbconvert --execute --to html myfigure.ipynb`

Exercise 1: Explore the command line options to remove code cells https://nbconvert.readthedocs.io/en/latest/config_options.html#cli-flags-and-aliases 

Exercise 2: Hide specific cells using cell metadata https://nbconvert.readthedocs.io/en/latest/removing_cells.html#removing-cells-inputs-or-outputs

## Other tools

If you plan on building a more sophisticated website, the pattern is the same! But definitely check out these tools that add a lot of functionality such as contents navigation, search, image/output management, cross-referencing, extended markdown features and nice styling just to name a few!

* https://mystmd.org
* https://jupyterbook.org
* https://quartopub.com
