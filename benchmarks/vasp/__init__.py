import os

from settings import PBS_NP, VASP_MODULE
from benchmarks.case import Case


class VASPCase(Case):
    def __init__(self, name, type, config, work_dir):
        super(VASPCase, self).__init__(name, type, config, work_dir)

    def _get_default_config(self):
        """
        Returns a default config for the case. It will be merged by the passed config.

        Returns:
            dict
        """
        default_config = super(VASPCase, self)._get_default_config()
        default_config.update({
            "module": VASP_MODULE,
            "command": f"mpirun -np {PBS_NP} vasp &> {self.stdout}",
        })
        return default_config

    def prepare(self):
        """
        Prepares the case for execution:
            - Creates working directory
            - Creates input files
            - Create job script file
            - Creates POTCAR from given pseudopotentials
        """
        super(VASPCase, self).prepare()
        pseudos = " ".join(self.config.get("pseudos", []))
        os.system(" ".join(("cat", pseudos, ">", os.path.join(self.work_dir, "POTCAR"))))

    def _get_application_context(self):
        """
        Returns the context to render the templates.

        Returns:
            dict
        """
        return {
            "kgrid": self.config["kgrid"],
            "nodes": self.config["nodes"]
        }
