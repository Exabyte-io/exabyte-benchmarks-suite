RMS_TEMPLATE = """#!/bin/bash

#pbs -n {{ NAME }}
#pbs -j oe
#pbs -l nodes={{ NODES }}
#pbs -l ppn={{ PPN }}
#pbs -q {{ QUEUE }}
#pbs -l walltime={{ WALLTIME }}
#pbs -m {{ NOTIFY }}
#pbs -m {{ EMAIL }}

module add {{ MODULE }}
cd $PBS_O_WORKDIR

{{ SHARED_COMMAND }}

{{ COMMAND }}
"""
