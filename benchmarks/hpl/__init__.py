from settings import PPN, HPL_MODULE


def get_hpl_config(nodes, n, nb, p, q, prefix="hpl"):
    return {
        "NAME": "-".join((prefix, str(nodes))),
        "NODES": nodes,
        "MODULE": HPL_MODULE,
        "N": n,
        "NB": nb,
        "P": p,
        "Q": q,
        "COMMAND": "mpirun -np $PBS_NP xhpl &> hpl-`date +'%s'`.log",
        "INPUTS": [
            {
                "NAME": "HPL.dat",
                "TEMPLATE": "templates/HPL.dat"
            }
        ]
    }


HPL_CASES = [
    get_hpl_config(1, 200448, 192, 6, 6),
    get_hpl_config(2, 283776, 192, 8, 9),
    get_hpl_config(4, 401280, 192, 12, 12),
    get_hpl_config(8, 567552, 192, 16, 18),
]
