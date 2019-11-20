# TomoPy Short Course
Lead by Daniel Ching from The US Department of Energy’s Argonne National Laboratory at ICTMS 2019, Cairns, Australia

## Summary
In a 90 minute interactive session, we will learn to reconstruct three-dimensional images from two-dimensional projections using TomoPy, the open-source Python package for tomographic data processing and image reconstruction. The course assumes some knowledge of x-ray computed tomography, but only minimal knowledge of computer programming. Topics covered include common steps to reconstruct x-ray computed tomography data and how to choose a reconstruction algorithm.

## Materials
The short course requires a 64-bit computer running Windows 10, macOS, or Linux, and either internet access or for the instructor to bring the custom pre-built miniconda installers for distribution.

## Source-code Organization
This repository contains the source files to run the workshop.

`activities/` contains a conda environment yaml listing required packages, markdown pages, jupyter notebooks, and materials for each of the course activities. Activities 5...7 may also be explored online using [Binder](https://mybinder.org/v2/gh/tomography/tomopy-short-course/master).

`solutions/` contains example scripts for the two final activities.

`citations.bib` contains citations for related works.

`build/` contains `construct.yaml` which is for using the [conda constructor](https://github.com/conda/constructor) to create a custom miniconda installer which comes with TomoPy and jupyter notebook preinstalled (no internet needed).

## Anonymous Survey

https://forms.gle/NK5yhVq5yGcAvRKs6
