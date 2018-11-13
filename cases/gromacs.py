import os
from copy import deepcopy

from benchmarks.utils import read_json

GROMACS_CASES = []
CWD = os.path.dirname(__file__)

# generate Gromacs cases
for input_ in ["model-1", "model-2", "model-3", "model-4"]:
    for config in read_json(os.path.join(CWD, "scaling-params.json")):
        config.update({
            "inputs": [
                {
                    "name": "md.tpr",
                    "template": "benchmarks/gromacs/inputs/{}/md.tpr".format(input_)
                }
            ],
            "command": "source GMXRC.bash; mpirun -np $PBS_NP gmx_mpi_d mdrun -ntomp 1 -s md.tpr -deffnm md"
        })
        GROMACS_CASES.append({
            "name": "-".join((input_, "{0:0=2d}".format(config["nodes"]), "{0:0=2d}".format(config["ppn"]))),
            "type": "gromacs",
            "reference": "benchmarks.gromacs.GROMACSCase",
            "config": deepcopy(config)
        })
