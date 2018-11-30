import matplotlib.pyplot as plt


class Metric(object):
    """
    Base metric class.
    """

    def __init__(self, name, results):
        self.name = name
        self.results = results

    def config(self, site_names):
        """
        Returns the config that is passed to matplot.
        Override upon inheritance.

        Returns:
            dict
        """
        raise NotImplemented

    def plot(self, site_names):
        config = self.config(site_names)
        plt.xlabel(config["xLabel"])
        plt.ylabel(config["yLabel"])
        if config.get("title"): plt.title(config["title"])

        for item in config["series"]:
            plt.plot(item["xValues"], item["yValues"], label=item["name"])

        if config["legend"]: plt.legend()
        plt.show()
