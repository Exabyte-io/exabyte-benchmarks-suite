import os

from benchmarks.hpl.cases import HPL_CASES
from benchmarks.vasp.cases import VASP_CASES
from benchmarks.gromacs.cases import GROMACS_CASES
from benchmarks.espresso.cases import ESPRESSO_CASES

CASES = []
CWD = os.path.dirname(__file__)

# ADD YOUR CASES HERE
CASES.extend(HPL_CASES)
CASES.extend(VASP_CASES)
CASES.extend(GROMACS_CASES)
CASES.extend(ESPRESSO_CASES)
