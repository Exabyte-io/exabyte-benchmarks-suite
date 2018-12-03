import os

SITE_NAME = ""
SITE_LOCATION = ""

RUNTIME_FILE = "runtime"
CPU_INFO_FILE = "cpuinfo"
MEM_INFO_FILE = "meminfo"
RMS_JOB_FILE_NAME = "job.rms"
RESULTS_FILE_NAME = "results.json"
RESULTS_FILE_PATH = os.path.join(os.path.dirname(__file__), RESULTS_FILE_NAME)
RMS_JOB_FILE_PATH = os.path.join(os.path.dirname(__file__), RMS_JOB_FILE_NAME)

PUBLISH_RESULTS = True
REMOTE_SOURCE_API_URL = "https://us-central1-exabyte-io.cloudfunctions.net/Exabyte-Benchmarks-Results"

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

METRICS_REGISTRY = {
    "PerformancePerCore": "metrics.performance_per_core.PerformancePerCore"
}
