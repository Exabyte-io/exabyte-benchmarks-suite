import os
import re

from benchmarks.case import Case
from benchmarks.utils import read
from settings import HPL_MODULE, HPL_RESULT_REGEX


class HPLCase(Case):
    def __init__(self, name, config, work_dir):
        super(HPLCase, self).__init__(name, config, work_dir)

    def _get_default_config(self):
        """
        Returns a default config for the case. It will be merged by the passed config.

        Returns:
            dict
        """
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
        """
        Returns the context to render the HPL.dat file.

        Returns:
            dict
        """
        return {
            "N": self.config["N"],
            "NB": self.config["NB"],
            "P": self.config["P"],
            "Q": self.config["Q"]
        }

    def get_extra_params(self):
        """
        Parses the output and extracts the result.

        Returns:
            dict
        """
        results = ["-" for i in range(6)]
        if os.path.exists(self.stdout_file):
            content = read(os.path.join(self.work_dir, self.stdout))
            pattern = re.compile(HPL_RESULT_REGEX, re.I | re.MULTILINE)
            matches = pattern.findall(content)
            if matches: results = matches[0]
        return {
            "N": results[0],
            "NB": results[1],
            "P": results[2],
            "Q": results[3],
            "TIME": results[4],
            "GFLOPS": results[5]
        }
