from settings import VASP_MODULE, VASP_VERSION


def get_vasp_elb_config(nodes, prefix="elb"):
    return {
        "NAME": "-".join((prefix, str(nodes))),
        "NODES": nodes,
        "MODULE": VASP_MODULE,
        "COMMAND": """
            cp /export/share/pseudo/ba/gga/pbe/vasp/{0}/paw/sv/POTCAR POTCAR
            cp /export/share/pseudo/o/gga/pbe/vasp/{0}/paw/default/POTCAR POTCAR
            cp /export/share/pseudo/bi/gga/pbe/vasp/{0}/paw/default/POTCAR POTCAR
            mpirun -np $PBS_NP vasp &> vasp-`date +'%s'`.log
        """.format(VASP_VERSION),
        "kgrid": {
            "dimensions": [1, 1, 2],
            "shifts": [0, 0, 0],
        },
        "INPUTS": [
            {
                "NAME": "INCAR",
                "TEMPLATE": "templates/ELB-INCAR"
            },
            {
                "NAME": "POSCAR",
                "TEMPLATE": "POSCARS/Ba25Bi15O54"
            },
            {
                "NAME": "KPOINTS",
                "TEMPLATE": "templates/KPOINTS"
            }
        ]
    }


VASP_CASES = [
    get_vasp_elb_config(1),
    get_vasp_elb_config(2),
    get_vasp_elb_config(4),
    get_vasp_elb_config(8),
]
