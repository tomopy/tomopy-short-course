# Miniconda / Conda / Anaconda

> Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer. It was created for Python programs, but it can package and distribute software for any language.

We use Conda to distribute and provide updates for TomoPy. Conda is the package management program, Anaconda is a distribution that provides Conda and many packages pre-installed. Miniconda is a distribution that provides Conda and fewer pacakges pre-installed.

## Installing Conda

### With internet
1. Download [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. Follow the [installation instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

### Without internet
1. Your instructor has provided you with a Conda distribution called `TomoPyShortCourse-0.0.0-[OS-name]x86_64.[extension]`. You can install Conda using this executable.

#### Windows
2. Run the installer by clicking on it.

#### Unix
2. Run the installer using the terminal like so:
<!---
Calling bash directly means you don't need to change exec permissions on the file.
--->
```
bash TomoPyShortCourse[bla-bla-bla].sh
```

<!--- INSTRUCTOR ACTIVITY
Live demonstrate the installer on your own machine.
--->

## Conda environments
Conda environments are used to keep packages with conflicting dependencies separate. We recommend installing TomoPy into it's own environment.

## Conda channels
Like television channels, a Conda channel provides different sets of programs to users. You can watch the Big Bang Theory on many television channels, but they may offer different seasons of the show at different times.

# Installing TomoPy
The first time you install TomoPy, do this:

```
conda create -n [environment-name] tomopy dxchange -c conda-forge
```

This will create a new Conda environment named `[environment-name]` and install the most recent version of TomoPy and DXchange from the conda-forge channel.

Then you can activate the new environment using:

```
conda activate [environment-name]
```

In the future, you can get updates to TomoPy.

```
$ conda update tomopy -c conda-forge
```
