import os

from benchmarks.utils import read_json

HPL_CASES = []
CWD = os.path.dirname(__file__)

# Generate HPL cases
for config in read_json(os.path.join(CWD, "cases.json")):
    HPL_CASES.append({
        "name": "-".join(("hpl", "{0:0=2d}".format(config["nodes"]))),
        "type": "hpl",
        "reference": "benchmarks.hpl.HPLCase",
        "config": config
    })
