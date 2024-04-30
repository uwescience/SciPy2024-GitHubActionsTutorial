# Github Actions for Scientific Data Workflows

Tutorial presented at [SciPy 2024 Conference](https://www.scipy2024.scipy.org/)

Authors: Valentina Staneva, Quinn Brencher, Scott Henderson

## Abstract

In this tutorial we will introduce GitHub Actions to scientists as a tool for lightweight automation of scientific data workflows. We will demonstrate that GitHub Actions are not just a tool for software testing, but can be used in various ways to improve the reproducibility and impact of scientific analysis. Through a sequence of examples, we will demonstrate some of Github Actions' applications to scientific workflows, such as scheduled deployment of algorithms to sensor streams, updating visualizations based on new data, processing large datasets, model versioning and performance benchmarking. GitHub Actions can particularly empower Python scientific programmers who are not willing to build fully-fledged applications or set up complex computational infrastructure, but would like to increase the impact of their work. The goal is that participants will leave with their own ideas of how to integrate Github Actions in their own work. 

## Description:

GitHub Actions are quite popular within the software engineering community, but a scientific Python programmer may not have seen their use beyond a continuous integration framework for unit testing. We would like to increase their visibility through a scientific workflow lens. We will use examples that are relevant to the community: wrangling a messy realtime hydrophone data stream to display noise sounds from the Puget Sound (not far from the conference venue!) or processing hundreds of satellite radar images over glacial lakes in High-Mountain Asia to study  flood hazards. We assume no knowledge on Github Actions and will start slowly with a “Hello World” step, but build quickly to create complex and exciting workflows. We will also showcase their value for scientific collaborations across institutions as a means to share reproducible workflows and computing infrastructure.

## Prerequisites: 
GitHub account, familiarity with git, GitHub, and Python (conda, scipy, matplotlib), some maturity in manipulating scientific data and exposure to the challenges associated with it, ability to read code (our examples may use libraries not familiar to the audience, but the focus will be on the steps these libraries accomplish rather than the details)

## Installation Instructions: 
Participants can make edits from the GitHub interface, but if they are willing to make updates locally, they need to have a functioning git ([set up instructions](https://swcarpentry.github.io/git-novice/#installing-git))

## Outline

Outline:

* Overview of GitHub Actions and Workflows and their popular uses in Python software development (examples of testing, listing, packaging)(30 min)
	* We will explain the main components of GitHub Actions and associated terminology
	* We will summarize their typical uses in software development 
	* We will point to popular GitHub Actions used in Python software development and packaging (the focus of this tutorial will not be on them but rather on scientific pipelines)

* Setting up your first workflow: a scientific Python environment (20 min)
	* participants will update a workflow `.yml` file to create an environment with their favorite Python libraries
	* participants will inspect the github interface to see the workflow runs

* Scheduled algorithm deployment to a realtime stream (30 min)
	* we will deploy a typical scientific workflow: reading data, converting to a new format, and making a visualization
	* participants will update the deployment schedule to trigger a new workflow and will monitor the progress in the GitHub interface

* Break (10 min)

* Exporting results (30 min)
  	* participants will learn about various ways to store the results: 
		* caching
		* creating GitHub artifacts
  	  	* committing to GitHub
  	  	* storing to own storage
        * they will modify the code to make their own plot which will be automatically updated
  	* they will use either matplotlib or an interactive library such as plotly

* Update results on a webpage (30 min)
	* we will overview different ways to display scientific results on a webpage
	* we will demonstrate the workflow to deploy the webpage 
	* participants will rerender the webpage based on the updates in GitHub

* Large-scale data processing (30 min)
	* we will demonstrate a use-case of processing large data sets with Github Actions
	* participants will fiddle with problem size to understand the power and limits of the computational infrastructure
	* we will discuss connections to cluster/cloud computing

* Break (10 min)

* Model Versioning and Comparison (30 min) 
	* we will introduce how to leverage GitHub’s version control to version different models and performance
	* participants can contribute a new model and check its performance
	* we will discuss how this can be used as a community network to share methods and results

* Recap and Discussion (or buffer time)  (20 min)
	* we will have a discussion on potential uses of Github Actions within the work of the participants

# References
* [*GitHub Actions for Scientific Data Workflows*](https://github.com/valentina-s/GithubActionsTutorial-USRSE23), Valentina Staneva, [US-RSE 2023 Tutorial](https://us-rse.org/usrse23/program/tutorials/) 
* [*Characterizing glacial lake outburst flood hazard at regional scale using fused InSAR-speckle tracking surface displacement time series*](https://escience.washington.edu/2024-incubator-projects/), Quinn Brencher and Scott Henderson, eScience Institute Data Incubator Project, 2024, [[repo](https://github.com/relativeorbit/actions-batch-demo)]
* [*GitHub Actions Workflows for Scheduled Algorithm Deployment*], Dmitry Volodin, Jesse Lopez, Scott Veirs, Val Veirs, Valentina Staneva, Orcasound Google Summer Of Code 2021 Project, [[repo]](https://github.com/orcasound/orca-action-workflow)
