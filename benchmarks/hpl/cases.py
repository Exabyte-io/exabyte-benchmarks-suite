import os

from benchmarks.utils import read_json

HPL_CASES = []
CWD = os.path.dirname(__file__)

# Generate HPL cases
for config in read_json(os.path.join(CWD, "cases.json")):
    case_config = {
        "name": "-".join(("hpl", "{0:0=2d}".format(config["nodes"]))),
        "type": "hpl",
        "reference": "benchmarks.hpl.HPLCase",
    }
    case_config.update(config)
    HPL_CASES.append(case_config)
