#!/bin/bash

# RMS
QUEUE="OF"
CORES_PER_NODE="16"
EMAIL="mohammad@exabyte.io"

# HPL
HPL_BINARY_PATH="./xhpl"

# NETWORK
IMB_MPI1="./IMB-MPI1"

# MODULES
INTEL_MODULE="intel/i-174"
MKL_MODULE="mkl/i-174"
MPI_MODULE="mpi/impi-044"
ESPRESSO_MODULE="espresso/540-i-174-impi-044"
VASP_MODULE="vasp/544-i-174-impi-044"
GROMACS_MODULE="gromacs/514-i-174-impi-044-md"
GROMACS_GPU_MODULE="gromacs/20183-i-174-impi-044-gms"
