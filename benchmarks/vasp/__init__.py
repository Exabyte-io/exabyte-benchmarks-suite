from settings import VASP_MODULE, VASP_VERSION


def get_vasp_elb_config(nodes, ppn, prefix="elb"):
    return {
        "NAME": "-".join((prefix, "{0:0=2d}".format(nodes), "{0:0=2d}".format(ppn))),
        "NODES": nodes,
        "PPN": ppn,
        "MODULE": VASP_MODULE,
        "COMMAND": """
            cat /export/share/pseudo/ba/gga/pbe/vasp/{0}/paw/sv/POTCAR > POTCAR
            cat /export/share/pseudo/o/gga/pbe/vasp/{0}/paw/default/POTCAR >> POTCAR
            cat /export/share/pseudo/bi/gga/pbe/vasp/{0}/paw/default/POTCAR >> POTCAR
            mpirun -np $PBS_NP vasp &> vasp-`date +'%s'`.log
        """.format(VASP_VERSION),
        "KGRID": {
            "DIMENSIONS": [1, 1, 2],
            "SHIFTS": [0, 0, 0],
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
    get_vasp_elb_config(1, 4),
    get_vasp_elb_config(1, 8),
    get_vasp_elb_config(1, 12),
    get_vasp_elb_config(1, 16),
    get_vasp_elb_config(2, 4),
    get_vasp_elb_config(2, 8),
    get_vasp_elb_config(2, 12),
    get_vasp_elb_config(2, 16),
    get_vasp_elb_config(4, 4),
    get_vasp_elb_config(4, 8),
    get_vasp_elb_config(4, 12),
    get_vasp_elb_config(4, 16),
    get_vasp_elb_config(8, 4),
    get_vasp_elb_config(8, 8),
    get_vasp_elb_config(8, 12),
    get_vasp_elb_config(8, 16),
]
