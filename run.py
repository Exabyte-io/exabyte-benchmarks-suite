import os
import argparse

from tabulate import tabulate

from cases import CASES
from benchmarks.hpl import HPLCase
from benchmarks.vasp import VASPCase
from benchmarks.gromacs import GROMACSCase
from benchmarks.utils import get_class_by_refernce


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--prepare', action="store_true", help='prepare benchmarks')
    parser.add_argument('-e', '--execute', action="store_true", help='execute benchmarks')
    parser.add_argument('-r', '--results', action="store_true", help='extract benchmarks results')
    parser.add_argument('-t', '--type', dest="types", action="append", help='benchmark type')
    return parser.parse_args()


def print_results(cases, headers):
    results = [case.results() for case in cases]
    print tabulate(results, headers, tablefmt='grid', stralign='center')


def print_hpl_results(cases):
    hpl_cases = [case for case in cases if isinstance(case, HPLCase)]
    hpl_headers = ["NAME", "NODES", "PPN", "RUNTIME", "N", "NB", "P", "Q", "TIME", "GFLOPS"]
    print_results(hpl_cases, hpl_headers)


def print_vasp_results(cases):
    vasp_cases = [case for case in cases if isinstance(case, VASPCase)]
    vasp_headers = ["NAME", "NODES", "PPN", "RUNTIME"]
    print_results(vasp_cases, vasp_headers)


def print_gromacs_results(cases):
    gromacs_cases = [case for case in cases if isinstance(case, GROMACSCase)]
    gromacs_headers = ["NAME", "NODES", "PPN", "RUNTIME"]
    print_results(gromacs_cases, gromacs_headers)


if __name__ == '__main__':
    cases = []
    args = parse_arguments()
    cwd = os.path.dirname(__file__)
    for case in CASES:
        if args.types and case["type"] not in args.types: continue
        for input_ in case["config"].get("inputs", []):
            if input_["template"]: input_["template"] = os.path.join(cwd, input_["template"])
        dir_ = os.path.join(cwd, "benchmarks", case["type"], "cases", case["name"])
        cases.append(get_class_by_refernce(case["reference"])(case["name"], case["config"], dir_))

    if args.execute: [case.execute() for case in cases]
    if args.prepare: [case.prepare() for case in cases]
    if args.results:
        print_hpl_results(cases)
        print_vasp_results(cases)
        print_gromacs_results(cases)
