import os
from copy import deepcopy

from benchmarks.utils import read_json

CASES = []
CWD = os.path.dirname(__file__)

# generate HPL cases
HPL_CASES = read_json(os.path.join(CWD, "hpl.json"))
for config in HPL_CASES:
    CASES.append({
        "name": "-".join(("hpl", "{0:0=2d}".format(config["nodes"]))),
        "type": "hpl",
        "reference": "benchmarks.hpl.HPLCase",
        "config": config
    })

# generate VASP-ELB cases
VASP_ELB_CASES = read_json(os.path.join(CWD, "scaling-params.json"))
for config in VASP_ELB_CASES:
    config.update(read_json(os.path.join(CWD, "vasp-elb.json")))
    CASES.append({
        "name": "-".join(("elb", "{0:0=2d}".format(config["nodes"]), "{0:0=2d}".format(config["ppn"]))),
        "type": "vasp",
        "reference": "benchmarks.vasp.VASPCase",
        "config": config
    })

# generate VASP-KPT cases
VASP_KPT_CASES = read_json(os.path.join(CWD, "scaling-params.json"))
for config in VASP_KPT_CASES:
    config.update(read_json(os.path.join(CWD, "vasp-kpt.json")))
    CASES.append({
        "name": "-".join(("kpt", "{0:0=2d}".format(config["nodes"]), "{0:0=2d}".format(config["ppn"]))),
        "type": "vasp",
        "reference": "benchmarks.vasp.VASPCase",
        "config": config
    })

# generate Gromacs cases
GROMACS_CASES = read_json(os.path.join(CWD, "scaling-params.json"))
for input_ in ["model-1", "model-2", "model-3", "model-4"]:
    for config in GROMACS_CASES:
        config.update({
            "inputs": [
                {
                    "name": "md.tpr",
                    "template": "benchmarks/gromacs/inputs/{}.tpr".format(input_)
                }
            ],
            "command": "source GMXRC.bash; mpirun -np $PBS_NP gmx_mpi_d mdrun -ntomp 1 -s md.tpr -deffnm md"
        })
        CASES.append({
            "name": "-".join((input_, "{0:0=2d}".format(config["nodes"]), "{0:0=2d}".format(config["ppn"]))),
            "type": "gromacs",
            "reference": "benchmarks.gromacs.GROMACSCase",
            "config": deepcopy(config)
        })
