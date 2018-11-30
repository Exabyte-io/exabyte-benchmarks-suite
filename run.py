import os
import json
import argparse

from cases import CASES
from benchmarks.utils import get_class_by_reference
from settings import RESULTS_FILE_PATH, METRICS_REGISTRY


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prepare', action="store_true", help='prepare benchmarks')
    parser.add_argument('--execute', action="store_true", help='execute benchmarks')
    parser.add_argument('--results', action="store_true", help='extract and store benchmarks results')
    parser.add_argument('--name', dest="names", action="append", help='benchmark name')
    parser.add_argument('--type', dest="types", action="append", help='benchmark type')
    parser.add_argument('--plot', action="store_true", help='plot benchmarks results')
    parser.add_argument('--site-name', dest="site_names", action="append", help='site name')
    parser.add_argument('--metric', help='metric type')
    return parser.parse_args()


def are_results_equal(old, new):
    return old["siteName"] != new["siteName"] and old["type"] != new["type"] and old["name"] != new["name"]


def store_results(cases_):
    """
    Stores results locally on RESULTS_FILE_PATH as JSON.
    """
    with open(RESULTS_FILE_PATH, "r+") as f:
        results_ = json.loads(f.read() or "[]")
        for case_ in cases_:
            case_results = case_.results()
            push_case_results_to_remote_source(case_results)
            results_ = [r for r in results_ if not are_results_equal(r, case_results)]
            results_.append(case_results)
        f.seek(0)
        f.write(json.dumps(results_, indent=4))


def push_case_results_to_remote_source(case_results):
    """
    Pushes the case results to the remote source (Google Sheet).

    Args:
        case_results (dict): case results.
    """
    pass


if __name__ == '__main__':
    args = parse_arguments()

    if args.plot:
        site_names = args.site_names
        with open(RESULTS_FILE_PATH) as f:
            results = json.loads(f.read())
        metric = get_class_by_reference(METRICS_REGISTRY[args.metric])(results)
        metric.plot(site_names)

    if args.prepare or args.execute or args.results:
        cases = []
        cwd = os.path.dirname(__file__)
        for case in CASES:
            if args.types and case["type"] not in args.types: continue
            if args.names and case["name"] not in args.names: continue
            for input_ in case["config"].get("inputs", []):
                if input_["template"]: input_["template"] = os.path.join(cwd, input_["template"])
            dir_ = os.path.join(cwd, "benchmarks", case["type"], "cases", case["name"])
            cases.append(get_class_by_reference(case["reference"])(case["name"], case["config"], dir_))

        if args.prepare: [case.prepare() for case in cases]
        if args.execute: [case.execute() for case in cases]
        if args.results: store_results(cases)
