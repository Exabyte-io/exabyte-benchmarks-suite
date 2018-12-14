import os

RUNTIME_FILE = "runtime"
RMS_JOB_FILE_NAME = "job.rms"
RMS_JOB_TEMPLATE = os.path.join(os.path.dirname(__file__), "templates/job.rms")

# RMS
PPN = 36
QUEUE = "OF"
NOTIFY = "abe"
WALLTIME = "05:00:00"
EMAIL = "mohammad@exabyte.io"
DEFAULT_RMS_CONFIG = {
    "NODES": 1,
    "PPN": PPN,
    "QUEUE": QUEUE,
    "WALLTIME": WALLTIME,
    "NOTIFY": NOTIFY,
    "EMAIL": EMAIL,
    "RUNTIME_FILE": RUNTIME_FILE,
}

# MODULES
IMB_MODULE = "imb"
MKL_MODULE = "mkl/i-174"
MPI_MODULE = "mpi/impi-044"
INTEL_MODULE = "intel/i-174"
HPL_MODULE = "hpl/22-i-174-impi-044"
VASP_MODULE = "vasp/544-i-174-impi-044"
ESPRESSO_MODULE = "espresso/540-i-174-impi-044"
GROMACS_MODULE = "gromacs/514-i-174-impi-044-md"
GROMACS_GPU_MODULE = "gromacs/20183-i-174-impi-044-gms"
