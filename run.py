import os
import argparse

from jinja2 import Template

from settings import *
from templates.rms import RMS_TEMPLATE


def parse_arguments():
    parser = argparse.ArgumentParser()
    return parser.parse_args()


def prepare_case(benchmark_, case_):
    case_path = os.path.join(BENCHMARKS_DIR, benchmark_, CASES_DIR, case_["NAME"])
    os.system("mkdir -p {}".format(case_path))
    case_["SHARED_COMMAND"] = SHARED_COMMAND
    with open(os.path.join(case_path, JOB_NAME), 'w+') as f:
        content = Template(RMS_TEMPLATE).render(**case_)
        f.write(content)
    for input in case_.get("INPUTS", []):
        with open(os.path.join(case_path, input["NAME"]), 'w+') as f:
            content = Template(input["TEMPLATE"]).render(**case_)
            f.write(content)
    os.system("cd {}; qsub {}".format(case_path, JOB_NAME))


if __name__ == '__main__':
    args = parse_arguments()
    for benchmark, cases in BENCHMARKS.iteritems():
        [prepare_case(benchmark, case) for case in cases]
