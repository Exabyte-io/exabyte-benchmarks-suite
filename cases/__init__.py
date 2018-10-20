import os

from benchmarks.utils import read_json

CASES = []
CWD = os.path.dirname(__file__)

HPL_CASES = read_json(os.path.join(CWD, "hpl.json"))
for config in HPL_CASES:
    CASES.append({
        "name": "-".join(("hpl", "{0:0=2d}".format(config["nodes"]))),
        "type": "hpl",
        "reference": "benchmarks.hpl.HPLCase",
        "config": config
    })

VASP_ELB_CASES = read_json(os.path.join(CWD, "vasp-elb.json"))
for config in VASP_ELB_CASES:
    config.update(read_json(os.path.join(CWD, "vasp-elb-default.json")))
    CASES.append({
        "name": "-".join(("elb", "{0:0=2d}".format(config["nodes"]), "{0:0=2d}".format(config["ppn"]))),
        "type": "vasp",
        "reference": "benchmarks.vasp.VASPCase",
        "config": config
    })

VASP_KPT_CASES = read_json(os.path.join(CWD, "vasp-kpt.json"))
for config in VASP_KPT_CASES:
    config.update(read_json(os.path.join(CWD, "vasp-kpt-default.json")))
    CASES.append({
        "name": "-".join(("kpt", "{0:0=2d}".format(config["nodes"]), "{0:0=2d}".format(config["ppn"]))),
        "type": "vasp",
        "reference": "benchmarks.vasp.VASPCase",
        "config": config
    })

ESPRESSO_CASES = read_json(os.path.join(CWD, "espresso.json"))
for config in ESPRESSO_CASES:
    CASES.append({
        "name": config["name"],
        "type": "espresso",
        "reference": "benchmarks.espresso.ESPRESSOCase",
        "config": config
    })

GROMACS_CASES = read_json(os.path.join(CWD, "gromacs.json"))
for config in GROMACS_CASES:
    CASES.append({
        "name": config["name"],
        "type": "gromacs",
        "reference": "benchmarks.gromacs.GROMACSCase",
        "config": config
    })
