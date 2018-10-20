import os

from benchmarks.case import Case
from settings import HPL_MODULE


class HPLCase(Case):
    def __init__(self, name, config, work_dir):
        super(HPLCase, self).__init__(name, config, work_dir)

    def _get_default_config(self):
        default_config = super(HPLCase, self)._get_default_config()
        default_config.update({
            "module": HPL_MODULE,
            "command": "mpirun -np $PBS_NP xhpl &> hpl-`date +'%s'`.log",
            "inputs": [
                {
                    "name": "HPL.dat",
                    "template": os.path.join(os.path.dirname(__file__), "templates/HPL.dat")
                }
            ]
        })
        return default_config

    def _get_application_context(self):
        return {
            "N": self.config["N"],
            "NB": self.config["NB"],
            "P": self.config["P"],
            "Q": self.config["Q"]
        }
