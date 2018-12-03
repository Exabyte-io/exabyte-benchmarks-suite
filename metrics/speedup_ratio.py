from metrics import Metric


class SpeedupRatio(Metric):
    """
    Speedup ratio metric class.
    """

    def __init__(self, results):
        super(SpeedupRatio, self).__init__("SpeedupRatio", results)

    def series(self, site_names):
        series = []
        for site_name in site_names:
            results = [r for r in self.results if r["siteName"] == site_name and r["type"] == "hpl"]
            single_node_performance = next((r["GFLOPS"] for r in results if r["nodes"] == 1))
            series.append({
                "name": site_name,
                "xValues": [r["nodes"] for r in results],
                "yValues": [r["GFLOPS"] / (r["nodes"] * single_node_performance) for r in results]
            })
        return series

    def config(self, site_names):
        series = self.series(site_names)
        return {
            "yLabel": "Speedup Ratio",
            "xLabel": 'Number Of Nodes',
            "series": series,
            "legend": len(series) > 1,
        }
