import os

# Name of the site where benchmarks are run. Should not contain space.
# Should contain the cloud provider, company and cluster name and should be unique to identify the site.
# SITE_NAME = "AWS-t2.nano-16nodes"
SITE_NAME = ""

# Name of the location where the benchmarks are run. Should contain information about the location of the SITE.
# SITE_LOCATION = "us-west-1b"
SITE_LOCATION = ""

# Name of the files to store the benchmark runtime, CPU and Memory info respectively.
RUNTIME_FILE = "runtime"
CPU_INFO_FILE = "cpuinfo"
MEM_INFO_FILE = "meminfo"

# Name of the file containing the job RMS template.
RMS_JOB_FILE_NAME = "job.rms"
RMS_JOB_FILE_PATH = os.path.join(os.path.dirname(__file__), RMS_JOB_FILE_NAME)

# Name of the JSON file to store the benchmark results.
RESULTS_FILE_NAME = "results.json"
RESULTS_FILE_PATH = os.path.join(os.path.dirname(__file__), "results", RESULTS_FILE_NAME)

# Whether to publish the results to:
# https://docs.google.com/spreadsheets/d/1oBHR8bp9q86MOxGYXcvUWHZa8KiC-uc_qX-UF1iqf-Y/edit
# Set it to True to enable it.
PUBLISH_RESULTS = False

# Google Cloud Function endpoint to send the benchmark results to.
REMOTE_SOURCE_API_URL = "https://us-central1-exabyte-io.cloudfunctions.net/Exabyte-Benchmarks-Results"

# Resource Management System (RMS) settings for PBS/Torque. Adjust settings to accommodate for other resource managers.
# http://docs.adaptivecomputing.com/torque/6-1-0/adminGuide/help.htm#topics/torque/2-jobs/submittingManagingJobs.htm
PPN = 1
QUEUE = "queue1"
WALLTIME = "05:00:00"
NOTIFY = "BEGIN, END, FAIL"
EMAIL = "mohammad@exabyte.io"
DEFAULT_RMS_CONFIG = {
    "NODES": 1,
    "PPN": PPN,
    "QUEUE": QUEUE,
    "WALLTIME": WALLTIME,
    "RUNTIME_FILE": RUNTIME_FILE,
    "NOTIFY": NOTIFY,
    "EMAIL": EMAIL
}

# Name of qsub command
QSUB_COMMAND = "sbatch"

# Argument of -np option of mpirun (computed from P*Q for HPL benchmark)
PBS_NP = 1

# Environment Settings
# HPL_ENVIRONMENT = '''
# module load intelmpi
# export PATH=$PATH:/home/ubuntu/hpl/bin/linux
# '''
HPL_ENVIRONMENT = "module add hpl/22-i-174-impi-044"
VASP_ENVIRONMENT = "module add vasp/535-i-174-impi-044"
ESPRESSO_ENVIRONMENT = "module add espresso/540-i-174-impi-044"
GROMACS_ENVIRONMENT = "module add gromacs/20183-i-174-impi-044-md"

# Regular expressions to extract the HPL results (N, NB, P, Q, TIME and GFLOPS)
REGEX = {
    'int': r'[+-]?\d+',
    'double': r'[-+]?\d*\.\d+(?:[eE][-+]?\d+)?',
}
HPL_RESULT_REGEX = r'.*\s+({0})\s+({0})\s+({0})\s+({0})\s+({1})\s+({1})'.format(REGEX["int"], REGEX["double"])

# Metric registry: key => metric name in CamelCase, value => metric class reference
METRICS_REGISTRY = {
    "SpeedupRatio": "metrics.speedup_ratio.SpeedupRatio",
    "PerformancePerCore": "metrics.performance_per_core.PerformancePerCore",
}

# Specifies nodes and ppn configurations.
# Cases are generated for gromacs and vasp all combinations.
NODES_CONFIGURATION = [1, 2, 4, 8]
PPN_CONFIGURATION = [4, 8, 12, 16]
