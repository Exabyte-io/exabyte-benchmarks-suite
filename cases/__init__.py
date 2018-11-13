import os

from cases.hpl import HPL_CASES
from cases.vasp import VASP_CASES
from cases.gromacs import GROMACS_CASES
from cases.espresso import ESPRESSO_CASES

CASES = []
CWD = os.path.dirname(__file__)

# ADD YOUR CASES HERE
CASES.extend(HPL_CASES)
CASES.extend(VASP_CASES)
CASES.extend(GROMACS_CASES)
CASES.extend(ESPRESSO_CASES)
