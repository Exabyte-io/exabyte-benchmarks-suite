#!/bin/bash

source ../../../../env.sh

cat > job.pbs << EOF
#!/bin/bash

#PBS -N PINGPONG
#PBS -j oe
#PBS -l nodes=2
#PBS -l ppn=1
#PBS -q ${QUEUE}
#PBS -l walltime=01:00:00
#PBS -m abe
#PBS -M ${EMAIL}

module add ${INTEL_MODULE} ${MKL_MODULE} ${MPI_MODULE}

cd \${PBS_O_WORKDIR}
mpirun -np \${PBS_NP} ${IMB_MPI1} pingpong > pingpong.out

EOF

qsub job.pbs
