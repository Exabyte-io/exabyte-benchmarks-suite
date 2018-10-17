#!/bin/bash

# TODO: automate HPL.dat generation

source ../../env.sh

for NODECT in `ls cases`; do

mkdir -p cases/${NODECT}
cd cases/${NODECT}

cat > job.pbs << EOF
#!/bin/bash

#PBS -N HPL-${NODECT}
#PBS -j oe
#PBS -l nodes=${NODECT}
#PBS -l ppn=${CORES_PER_NODE}
#PBS -q ${QUEUE}
#PBS -l walltime=05:00:00
#PBS -m abe
#PBS -M ${EMAIL}

module add ${INTEL_MODULE} ${MKL_MODULE} ${MPI_MODULE}

cd \${PBS_O_WORKDIR}
mpirun -np \${PBS_NP} ${HPL_BINARY_PATH} &> HPL.log

EOF

qsub job.pbs

cd -

done
