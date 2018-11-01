import os

RUNTIME_FILE = "runtime"
RMS_JOB_FILE_NAME = "job.rms"
RMS_JOB_TEMPLATE_FILE = os.path.join(os.path.dirname(__file__), "job.rms")

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
QSUB_COMMAND = "qsub"

# MODULES
HPL_MODULE = "hpl/22-i-174-impi-044"
VASP_MODULE = "vasp/535-i-174-impi-044"
ESPRESSO_MODULE = "espresso/540-i-174-impi-044"
GROMACS_MODULE = "gromacs/20183-i-174-impi-044-md"

REGEX = {
    'int': r'[+-]?\d+',
    'double': r'[-+]?\d*\.\d+(?:[eE][-+]?\d+)?',
}
HPL_RESULT_REGEX = r'.*\s+({0})\s+({0})\s+({0})\s+({0})\s+({1})\s+({1})'.format(REGEX["int"], REGEX["double"])
