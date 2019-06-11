"""Capstone Project: Write your own script!

In this file, write your own reconstruction script to do the following:

1. Load a dataset using dxchange.

2. Use the find center function to find the rotation center.
"""

import tomopy
import dxchange

if __name__ == '__main__':
    data, flat, dark, theta = dxchange.read_aps_32id(
        fname='activities/data/data-simulated.h5'
    )
    print(tomopy.find_center(tomo=data, theta=theta, ind=5, tol=0.1))
