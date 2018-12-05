import os

from settings import NODES_CONFIGURATION, PPN_CONFIGURATION

GROMACS_CASES = []
CWD = os.path.dirname(__file__)

# Generate GROMACS cases
for input_ in ["model-1", "model-2", "model-3", "model-4"]:
    for nodes in NODES_CONFIGURATION:
        for ppn in PPN_CONFIGURATION:
            config = {
                "name": "-".join((input_, "{0:0=2d}".format(nodes), "{0:0=2d}".format(ppn))),
                "type": "gromacs",
                "reference": "benchmarks.gromacs.GROMACSCase",
                "config": {
                    "nodes": nodes,
                    "ppn": ppn,
                    "inputs": [
                        {
                            "name": "md.tpr",
                            "template": "benchmarks/gromacs/inputs/{}/md.tpr".format(input_)
                        }
                    ],
                    "command": "source GMXRC.bash; mpirun -np $PBS_NP gmx_mpi_d mdrun -ntomp 1 -s md.tpr -deffnm md"
                }
            }
            GROMACS_CASES.append(config)
