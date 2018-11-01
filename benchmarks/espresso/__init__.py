import os

from benchmarks.case import Case
from settings import ESPRESSO_MODULE


class ESPRESSOCase(Case):
    def __init__(self, name, config, work_dir):
        super(ESPRESSOCase, self).__init__(name, config, work_dir)

    def _get_default_config(self):
        """
        Returns a default config for the case. It will be merged by the passed config.

        Returns:
            dict
        """
        default_config = super(ESPRESSOCase, self)._get_default_config()
        default_config.update({
            "module": ESPRESSO_MODULE
        })
        return default_config

    def prepare(self):
        """
        Prepares the case for execution:
            - Creates working directory
            - Creates input files
            - Create job script file
            - Creates pseudopotential symlinks.
        """
        super(ESPRESSOCase, self).prepare()
        pseudo_dir_path = os.path.join(self.work_dir, 'pseudo')
        for pseudo in self.config.get("pseudos", []):
            os.symlink(pseudo, os.path.join(pseudo_dir_path, os.path.basename(pseudo)))

    def _get_application_context(self):
        """
        Returns the context to render the templates.

        Returns:
            dict
        """
        return {}
