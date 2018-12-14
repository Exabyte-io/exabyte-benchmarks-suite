from settings import GROMACS_MODULE
from benchmarks.case import Case, os
from benchmarks.utils import read, write


class GROMACSCase(Case):
    def __init__(self, name, config, work_dir):
        super(GROMACSCase, self).__init__(name, config, work_dir)

    def _get_default_config(self):
        default_config = super(GROMACSCase, self)._get_default_config()
        default_config.update({
            "module": GROMACS_MODULE
        })
        return default_config

    def _create_input_files(self):
        for input_ in self.config["inputs"]:
            write(os.path.join(self.work_dir, input_["name"]), read(input_["template"]))
