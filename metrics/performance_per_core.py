from metrics import Metric


class PerformancePerCore(Metric):
    """
    Performance Per Core metric class.
    """

    def __init__(self, results):
        super(PerformancePerCore, self).__init__("PerformancePerCore", results)

    def series(self, site_names):
        series = []
        if not site_names: site_names = self.get_all_site_names()
        for site_name in site_names:
            results = [r for r in self.results if r["siteName"] == site_name and r["type"] == "hpl"]
            series.append({
                "name": site_name,
                "xValues": [r["nodes"] for r in results],
                "yValues": [float(r["GFLOPS"]) / (r["nodes"] * r["ppn"]) for r in results]
            })
        return series

    def config(self, site_names):
        series = self.series(site_names)
        return {
            "yLabel": "Performance Per Core (GFLOPS)",
            "xLabel": 'Number Of Nodes',
            "series": series,
            "legend": len(series) > 1,
        }
