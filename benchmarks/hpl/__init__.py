import os
import re

from benchmarks.case import Case
from benchmarks.utils import read
from settings import HPL_MODULE, HPL_RESULT_REGEX


class HPLCase(Case):
    def __init__(self, name, config, work_dir):
        super(HPLCase, self).__init__(name, config, work_dir)

    def _get_default_config(self):
        default_config = super(HPLCase, self)._get_default_config()
        default_config.update({
            "module": HPL_MODULE,
            "command": "mpirun -np $PBS_NP xhpl &> {}".format(self.stdout),
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

    def results(self):
        result = super(HPLCase, self).results()
        hpl_result = ["-", "-", "-", "-", "-", "-"]
        if os.path.exists(self.stdout_file):
            content = read(os.path.join(self.work_dir, self.stdout))
            pattern = re.compile(HPL_RESULT_REGEX, re.I | re.MULTILINE)
            matches = pattern.findall(content)
            if matches: hpl_result = matches[0]
        result.extend(hpl_result)
        return result
