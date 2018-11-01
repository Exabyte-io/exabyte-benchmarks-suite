import os
import argparse

from tabulate import tabulate

from cases import CASES
from benchmarks.utils import get_class_by_refernce


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--prepare', action="store_true", help='prepare benchmarks')
    parser.add_argument('-e', '--execute', action="store_true", help='execute benchmarks')
    parser.add_argument('-n', '--name', dest="names", action="append", help='benchmark name')
    parser.add_argument('-t', '--type', dest="types", action="append", help='benchmark type')
    parser.add_argument('-r', '--results', action="store_true", help='extract benchmarks results')
    return parser.parse_args()


if __name__ == '__main__':
    cases = []
    args = parse_arguments()
    cwd = os.path.dirname(__file__)
    for case in CASES:
        if args.types and case["type"] not in args.types: continue
        if args.names and case["name"] not in args.names: continue
        for input_ in case["config"].get("inputs", []):
            if input_["template"]: input_["template"] = os.path.join(cwd, input_["template"])
        dir_ = os.path.join(cwd, "benchmarks", case["type"], "cases", case["name"])
        cases.append(get_class_by_refernce(case["reference"])(case["name"], case["config"], dir_))

    if args.execute: [case.execute() for case in cases]
    if args.prepare: [case.prepare() for case in cases]
    if args.results:
        for case in cases:
            results = case.results()
            print tabulate(results.values(), results.keys(), tablefmt='grid', stralign='center')
