import os

from benchmarks.utils import read_json

VASP_CASES = []
CWD = os.path.dirname(__file__)

# generate VASP-ELB cases
VASP_ELB_CASES = read_json(os.path.join(CWD, "scaling-params.json"))
for config in VASP_ELB_CASES:
    config.update(read_json(os.path.join(CWD, "vasp-elb.json")))
    VASP_CASES.append({
        "name": "-".join(("elb", "{0:0=2d}".format(config["nodes"]), "{0:0=2d}".format(config["ppn"]))),
        "type": "vasp",
        "reference": "benchmarks.vasp.VASPCase",
        "config": config
    })

# generate VASP-KPT cases
VASP_KPT_CASES = read_json(os.path.join(CWD, "scaling-params.json"))
for config in VASP_KPT_CASES:
    config.update(read_json(os.path.join(CWD, "vasp-kpt.json")))
    VASP_CASES.append({
        "name": "-".join(("kpt", "{0:0=2d}".format(config["nodes"]), "{0:0=2d}".format(config["ppn"]))),
        "type": "vasp",
        "reference": "benchmarks.vasp.VASPCase",
        "config": config
    })
