from benchmarks.case import Case
from settings import GROMACS_MODULE


class GROMACSCase(Case):
    def __init__(self, name, config, work_dir):
        super(GROMACSCase, self).__init__(name, config, work_dir)

    def _get_default_config(self):
        default_config = super(GROMACSCase, self)._get_default_config()
        default_config.update({
            "module": GROMACS_MODULE
        })
        return default_config
