# Miniconda / Conda / Anaconda

> Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer. It was created for Python programs, but it can package and distribute software for any language.

We use Conda to distribute and provide updates for TomoPy. Conda is the package management program, Anaconda is a distribution that provides Conda and many packages pre-installed. Miniconda is a distribution that provides Conda and fewer pacakges pre-installed.

## Conda environments
Conda environments are used to keep packages with conflicting dependencies separate. We recommend installing TomoPy into it's own environment.

## Conda channels
Like television channels, a Conda channel provides different sets of programs to users. You can watch the Big Bang Theory on many television channels, but they may offer different seasons of the show at different times.

<!--- INSTRUCTOR ACTIVITY
Live demonstrate the installer on your own machine.
--->

## ACTIVITY: Installing Conda

### With internet
1. Download [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. Follow the [installation instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

### Without internet
1. Your instructor has provided you with a Conda distribution called `TomoPyShortCourse-0.0.0-[OS-name]x86_64.[extension]`. You can install everything for this course using this executable.

## ACTIVITY: Installing TomoPy
For this short course you can create a Conda environment using the file called `short-course-env.yaml`. Open the Anaconda Prompt (Windows) or a Terminal (Unix) and run the following command:

```
conda env create -f short-course-env.yaml
```

This will create a new Conda environment named `tomopy-short-course` and install the most recent version of TomoPy along with some other packages used in this short course.

You can activate the new environment using:

```
conda activate [environment-name]
```

In the future, you can get updates to the active environment by using:

```
$ conda update tomopy -c conda-forge
```
