from templates.hpl import HPL_TEMPLATE

BENCHMARKS_DIR = "benchmarks"
CASES_DIR = "cases"
JOB_NAME = "job.rms"

# RMS
PPN = 36
QUEUE = "OF"
NOTIFY = "abe"
WALLTIME = "05:00:00"
EMAIL = "mohammad@exabyte.io"

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

SHARED_COMMAND = """
# export I_MPI_FABRICS=shm:dapl
# export I_MPI_DAPL_PROVIDER=ofa-v2-cma-roe-enp94s0f0
# export I_MPI_DYNAMIC_CONNECTION=0
"""


def get_hpl_config(nodes, n, nb, p, q, prefix="hpl"):
    return {
        "NAME": "-".join((prefix, str(nodes))),
        "NODES": nodes,
        "PPN": PPN,
        "QUEUE": QUEUE,
        "WALLTIME": WALLTIME,
        "NOTIFY": NOTIFY,
        "EMAIL": EMAIL,
        "MODULE": HPL_MODULE,
        "N": n,
        "NB": nb,
        "P": p,
        "Q": q,
        "COMMAND": "mpirun -np $PBS_NP xhpl &> hpl-`date +'%s'`.log",
        "INPUTS": [
            {
                "NAME": "HPL.dat",
                "TEMPLATE": HPL_TEMPLATE
            }
        ]
    }


BENCHMARKS = {
    "hpl": [
        get_hpl_config(1, 200448, 192, 6, 6),
        get_hpl_config(2, 283776, 192, 8, 9),
        get_hpl_config(4, 401280, 192, 12, 12),
        get_hpl_config(8, 567552, 192, 16, 18),
    ],
    "network": [
        {
            "NAME": "pingpong",
            "NODES": 2,
            "PPN": PPN,
            "QUEUE": QUEUE,
            "WALLTIME": WALLTIME,
            "NOTIFY": NOTIFY,
            "EMAIL": EMAIL,
            "MODULE": IMB_MODULE,
            "COMMAND": "mpirun -np $PBS_NP IMB-MPI1 pingpong > pingpong.out",
        }
    ],
    "vasp": [],
    "gromacs": [],
    "espresso": [],
}
