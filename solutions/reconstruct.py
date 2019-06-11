"""Capstone Project: Write your own script!

In this file, write your own reconstruction script to do the following:

1. Load a dataset using dxchange.

2. Apply one preprocessing algorithm to remove distortions.

3. Reconstruct the data using one direct method.

4. Reconstruct the data using one iterative algorithm. Use the direct
reconstruction as the initial guess for the iterative algorithm.

5. Save your reconstructed data using dxchange.
"""

import tomopy
import dxchange

if __name__ == '__main__':
    data, flat, dark, theta = dxchange.read_aps_32id(
        fname='activities/data/data-simulated.h5'
    )
    data = tomopy.median_filter(arr=data, axis=0)
    recon = tomopy.recon(tomo=data, theta=theta, algorithm='gridrec')
    recon = tomopy.recon(tomo=data, theta=theta, init_recon=recon,
                         algorithm='art', num_iter=10)
    dxchange.write_tiff_stack(fname='solutions/data/recon/full', data=recon,
                              dtype='float32', overwrite=True)
