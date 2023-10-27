# RBT350-HandsOn3-Tutorial

This is a basic python tutorial specifically designed for the RBT350 course. 

## Logistics
- **Date**: 10/27/2023
- **Time**: 5:00 to 6:00 pm
- **Location**: GDC 5.302

## Installation

### Virtual Environment
A virtual environment in Python is like a separate room for each of your projects. It keeps all the tools and materials that project needs, so they don't get mixed up with other projects. This helps you avoid problems and keeps everything organized.

Miniconda is like the toolbox that helps you create and manage these separate project rooms (virtual environments) for your Python work. Now install miniconda through [this link](https://docs.conda.io/en/latest/miniconda.html). Once that's done, create a conda environment for the project by running the terminal commands below. If you're on Windows, you will need to do this in the Anaconda Prompt Terminal. Those on Linux and MacOS can run the commands in a regular terminal. 
```
conda create --name py_basics python=3.8
conda activate py_basics
```
To activate the conda environment,
```
conda activate py_basics
```

### Jupyter Notebook
Jupyter notebooks are interactive documents where you can write and run code, view results, and include explanations and visualizations all in one place.
```
pip install notebook 
```

Running Jupyter notebooks,
```
jupyter notebook hands_on3_basics.ipynb
```
