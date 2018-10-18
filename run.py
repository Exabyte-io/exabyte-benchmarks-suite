import os
import argparse

from jinja2 import Template

from settings import *
from utils import read, write


def parse_arguments():
    parser = argparse.ArgumentParser()
    return parser.parse_args()


def prepare_case(benchmark_, case_):
    benchmark_dir = os.path.join(BENCHMARKS_DIR, benchmark_)
    cases_dir = os.path.join(benchmark_dir, CASES_DIR)
    case_dir = os.path.join(cases_dir, case_["NAME"])
    os.system("mkdir -p {}".format(case_dir))

    # populate the context
    context = GENERAL_CONFIG
    context.update(case_)

    # create job script
    job_path = os.path.join(case_dir, JOB_NAME)
    job_content = Template(read(JOB_TEMPLATE)).render(context)
    write(job_path, job_content)

    # create inputs
    for input_ in case_.get("INPUTS", []):
        template = read(os.path.join(benchmark_dir, input_["TEMPLATE"]))
        write(os.path.join(case_dir, input_["NAME"]), Template(template).render(context))

    # submit jobs
    os.system("cd {}; qsub {}".format(case_dir, JOB_NAME))


if __name__ == '__main__':
    args = parse_arguments()
    for benchmark, cases in BENCHMARKS.iteritems():
        [prepare_case(benchmark, case) for case in cases]
