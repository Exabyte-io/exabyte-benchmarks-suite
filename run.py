#!/usr/bin/python

import sys
import glob
import utils
import shutil
import os.path
import fileinput
import subprocess
from settings import *
from argparse import ArgumentParser


class RunTestStructure:
    """
    Runs a single test using files obtained from `origin` directory (run.py's first argument).  The outputs
    will be the output files of the application which can then be compared against the *.json files present
    under the workdir directory path.
    """

    def __init__(self, origin):
        """
            Initialize attributes based on settings.py and run script argument parsed into origin

            Args:
                origin (str): The 'origin' is path to a directory that contains a previously constructed
                    test case with application input files including a test structure.
        """
        self.origin = os.path.join(ROOT, origin)
        self.destination = self.origin.replace(INPDIR, OUTDIR)
        if 'vasp' in self.origin:
            self.application = 'vasp'
        elif 'espresso' in self.origin:
            self.application = 'espresso'
        else:
            raise ValueError('No application can be found in path')

    def prepare(self):
        """
            Prepares the directory structure and input files depending on user input
        """
        if os.path.isdir(self.destination):
            shutil.rmtree(self.destination)
        shutil.copytree(self.origin, self.destination, symlinks=True, ignore=None)

        if self.application == 'vasp':
            self.prepare_pseudo_vasp()
        elif self.application == 'espresso':
            self.prepare_pseudo_espresso()
        else:
            raise ValueError('Unsupported application for input preparation')

    def prepare_pseudo_vasp(self):
        """
        Concatenates files available at paths specified in a file into one POTCAR file
        """
        paths = utils.read_file_lines(os.path.join(self.origin, 'POTCAR.paths'))
        for path in paths:
            if not os.path.exists(path):
                raise ValueError('Path {} not found'.format(path))
        with open(os.path.join(self.destination, 'POTCAR'), 'w') as potcar:
            potcar.writelines(fileinput.input(paths))

    def prepare_pseudo_espresso(self):
        """
        Populates pseudopotential using paths specified in a file
        """
        paths = utils.read_file_lines(os.path.join(self.origin, 'pseudo.paths'))
        dictionary = {}
        infiles = glob.glob(os.path.join(self.destination, '*.in'))
        for index, path in enumerate(paths):
            for infile in infiles:
                dictionary['PSEUDO_DIR'] = os.path.dirname(path)
                dictionary['PSEUDO_' + str(index)] = os.path.basename(path)
                utils.replace_variables(dictionary, os.path.join(self.destination, infile))

    def run(self):
        """
        Sets up the environment and runs test
        """
        try:
            cmd = """
                cd {RUNDIR}
                module load {MODULE}
                sh workflow.sh
            """
            cmd = cmd.format(RUNDIR=self.destination, MODULE=MODULES[self.application])
            subprocess.check_call(cmd, shell=True)
        except:
            raise


def main():
    parser = ArgumentParser(description="run.py runs an example calculation based on the input directory")
    parser.add_argument("-d", dest="origin", required=True,
                        help="full path to a directory with files for testing", type=str)
    parser.add_argument('-r', dest='run', action='store_true')
    parser._optionals.title = "arguments"

    args = parser.parse_args()
    origin = args.origin
    utils.is_valid_file(parser, origin)

    test = RunTestStructure(origin)
    test.prepare()
    if args.run:
        test.run()

if __name__ == '__main__':
    main()
