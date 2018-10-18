from settings import IMB_MODULE

NETWORK_CASES = [
    {
        "NAME": "pingpong",
        "NODES": 2,
        "MODULE": IMB_MODULE,
        "COMMAND": "mpirun -np $PBS_NP IMB-MPI1 pingpong > pingpong.out",
    }
]
