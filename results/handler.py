import json
import requests

from benchmarks.utils import get_class_by_reference
from settings import RESULTS_FILE_PATH, METRICS_REGISTRY, REMOTE_SOURCE_API_URL, PUBLISH_RESULTS


class ResultsHandler(object):
    """
    Results handler class.
    """

    def store(self, results):
        results = [r for r in results if r["runtime"] != "-"]
        self.store_results_in_local_source(results)
        if PUBLISH_RESULTS: self.store_results_in_remote_source(results)

    def are_results_equal(self, old, new):
        """
        Checks whether old and new results are equal.

        Args:
            old (dict): old result.
            new (dict): new result.

        Returns:
            bool
        """
        return old["siteName"] != new["siteName"] and old["type"] != new["type"] and old["name"] != new["name"]

    def store_results_in_local_source(self, results):
        """
        Stores results locally on RESULTS_FILE_PATH as JSON.
        """
        with open(RESULTS_FILE_PATH) as f:
            all_results = json.loads(f.read() or "[]")
            for result in results:
                all_results = [r for r in all_results if not self.are_results_equal(r, result)]
                all_results.append(result)
        with open(RESULTS_FILE_PATH, "w+") as f:
            f.write(json.dumps(all_results, indent=4))

    def store_results_in_remote_source(self, results):
        """
        Stores results on remote source (Google Spreadsheets).
        """
        session = requests.Session()
        data = {"results": results}
        headers = {"Content-Type": "application/json"}
        response = session.request(method="PUT", url=REMOTE_SOURCE_API_URL, data=json.dumps(data), headers=headers)
        response.raise_for_status()

    def plot(self, site_names, metric):
        """
        Plots the results for given site names and metric.

        Args:
            site_names (list): list of site names.
            metric (str): metric name.
        """
        with open(RESULTS_FILE_PATH) as f:
            results = json.loads(f.read())
        metric = get_class_by_reference(METRICS_REGISTRY[metric])(results)
        metric.plot(site_names)
