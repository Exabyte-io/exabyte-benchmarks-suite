import os

from benchmarks.utils import read_json
from settings import NODES_CONFIGURATION, PPN_CONFIGURATION

VASP_CASES = []
CWD = os.path.dirname(__file__)

# Generate VASP cases
for nodes in NODES_CONFIGURATION:
    for ppn in PPN_CONFIGURATION:
        for type_ in ["elb", "kpt"]:
            config = {
                "name": "-".join((type_, "{0:0=2d}".format(nodes), "{0:0=2d}".format(ppn))),
                "type": "vasp",
                "reference": "benchmarks.vasp.VASPCase",
                "nodes": nodes,
                "ppn": ppn
            }
            config.update(read_json(os.path.join(CWD, "{}-cases.json".format(type_))))
