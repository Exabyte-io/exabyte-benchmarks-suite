#!/bin/bash

source ../../../../env.sh

cat > job.pbs << EOF
#!/bin/bash

#PBS -N VASP-HSE
#PBS -j oe
#PBS -l nodes=1
#PBS -l ppn=16
#PBS -q ${QUEUE}
#PBS -l walltime=02:00:00
#PBS -m abe
#PBS -M ${EMAIL}

module add ${VASP_MODULE}

cd \${PBS_O_WORKDIR}
cp /export/share/pseudo/si/gga/pbe/vasp/5.4/paw/default/POTCAR POTCAR

cp INCAR.1 INCAR
mpirun -np \${PBS_NP} vasp

cp INCAR.2 INCAR
mpirun -np \${PBS_NP} vasp

EOF

qsub job.pbs
