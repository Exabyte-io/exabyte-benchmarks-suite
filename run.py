import os
import argparse

from cases import CASES
from benchmarks.utils import get_class_by_refernce


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--prepare', action="store_true", help='prepare benchmarks')
    parser.add_argument('-e', '--execute', action="store_true", help='execute benchmarks')
    parser.add_argument('-r', '--results', action="store_true", help='extract benchmarks results')
    return parser.parse_args()


if __name__ == '__main__':
    classes = []
    cwd = os.path.dirname(__file__)
    for case in CASES:
        for input_ in case["config"].get("inputs", []):
            if input_["template"]: input_["template"] = os.path.join(cwd, input_["template"])
        dir_ = os.path.join(cwd, "benchmarks", case["type"], "cases", case["name"])
        classes.append(get_class_by_refernce(case["reference"])(case["name"], case["config"], dir_))

    args = parse_arguments()
    if args.execute: [cls.execute() for cls in classes]
    if args.prepare: [cls.prepare() for cls in classes]
    if args.results: [cls.results() for cls in classes]
