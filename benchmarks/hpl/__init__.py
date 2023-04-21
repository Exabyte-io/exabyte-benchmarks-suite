import os
import re

from benchmarks.case import Case
from benchmarks.utils import read
from settings import HPL_ENVIRONMENT, HPL_RESULT_REGEX


class HPLCase(Case):
    def __init__(self, name, type, config, work_dir):
        super(HPLCase, self).__init__(name, type, config, work_dir)

    def _get_case_config(self, config):
        """
        Returns a default config for the case. It will be merged by the passed config.

        Returns:
            dict
        """
        mpirun_np = config.get('P', 1) * config.get('Q', 1)
        default_config = super(HPLCase, self)._get_case_config(config)
        default_config.update({
            "environment": HPL_ENVIRONMENT,
            "command": f"mpirun -np {mpirun_np} xhpl &> {self.stdout}",
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

    def get_extra_results(self):
        """
        Returns extra results to add to the main results.

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
            "N": self.safely_convert(results[0], int),
            "NB": self.safely_convert(results[1], int),
            "P": self.safely_convert(results[2], int),
            "Q": self.safely_convert(results[3], int),
            "TIME": self.safely_convert(results[4], float),
            "GFLOPS": self.safely_convert(results[5], float)
        }
