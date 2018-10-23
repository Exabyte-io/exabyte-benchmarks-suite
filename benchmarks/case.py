from copy import deepcopy
from jinja2 import Template

from settings import *
from utils import read, write


class Case(object):
    def __init__(self, name, config, work_dir):
        """
        Base case class.

        Args:
            name (str): case name
            config (dict): case config.
            work_dir (str): case working directory.
        """
        self.name = name
        self.work_dir = work_dir
        self.stdout = ".".join((self.name, "log"))
        self.stdout_file = os.path.join(self.work_dir, self.stdout)
        self.config = deepcopy(self._get_default_config())
        self.config.update(config)

    def _get_default_config(self):
        """
        Returns a default config for the case. It will be merged by the passed config.

        Returns:
            dict
        """
        return {
            "queue": QUEUE,
            "nodes": 1,
            "ppn": PPN,
            "walltime": WALLTIME,
            "notify": NOTIFY,
            "email": EMAIL,
            "runtime_file": RUNTIME_FILE,
        }

    def _get_rms_context(self):
        """
        Returns the context to render the RMS template with.

        Returns:
            dict
        """
        return {
            "NAME": self.name,
            "QUEUE": self.config["queue"],
            "NODES": self.config["nodes"],
            "PPN": self.config["ppn"],
            "WALLTIME": self.config["walltime"],
            "NOTIFY": self.config["notify"],
            "EMAIL": self.config["email"],
            "MODULE": self.config["module"],
            "COMMAND": self.config["command"],
            "RUNTIME_FILE": self.config["runtime_file"],
        }

    def _get_application_context(self):
        """
        Returns the context to render the application-specific templates.

        Returns:
            dict
        """
        return {}

    def _create_work_dir(self):
        os.system("mkdir -p {}".format(self.work_dir))

    def _create_rms_job_script(self):
        job_path = os.path.join(self.work_dir, RMS_JOB_FILE_NAME)
        job_content = Template(read(RMS_JOB_TEMPLATE_FILE)).render(self._get_rms_context())
        write(job_path, job_content)

    def _create_input_files(self):
        for input_ in self.config["inputs"]:
            template = read(input_["template"])
            write(os.path.join(self.work_dir, input_["name"]),
                  Template(template).render(self._get_application_context()))

    def prepare(self):
        """
        Prepares the case for execution.
        """
        self._create_work_dir()
        self._create_input_files()
        self._create_rms_job_script()

    def execute(self):
        """
        Runs the case by submitting the job script to RMS.
        """
        os.system("cd {}; qsub {}".format(self.work_dir, RMS_JOB_FILE_NAME))

    def results(self):
        """
        Returns the results.
        """
        runtime = '-'
        runtime_file = os.path.join(self.work_dir, RUNTIME_FILE)
        if os.path.exists(runtime_file): runtime = read(runtime_file)
        return [self.name, self.config["nodes"], self.config["ppn"], runtime.rstrip("\n")]
