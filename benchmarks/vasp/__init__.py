import os

from settings import VASP_MODULE
from benchmarks.case import Case


class VASPCase(Case):
    def __init__(self, name, config, work_dir):
        super(VASPCase, self).__init__(name, config, work_dir)

    def _get_default_config(self):
        default_config = super(VASPCase, self)._get_default_config()
        default_config.update({
            "module": VASP_MODULE,
            "command": "mpirun -np $PBS_NP vasp &> {}".format(self.stdout),
        })
        return default_config

    def prepare(self):
        super(VASPCase, self).prepare()
        pseudos = " ".join(self.config.get("pseudos", []))
        os.system(" ".join(("cat", pseudos, ">", os.path.join(self.work_dir, "POTCAR"))))

    def _get_application_context(self):
        return {
            "kgrid": self.config["kgrid"],
            "nodes": self.config["nodes"]
        }
