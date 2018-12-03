# Exabyte Benchmarks

This repository provides a set of tools to benchmark hardware for distributed computing.

We use this tool to benchmark cloud provider systems agains the cases supported below, relevant for materials modeling:

- High-performance Linpack ([HPL](http://www.netlib.org/benchmark/hpl/))
- [Vienna ab-initio simulations provider](https://www.vasp.at/)
- [GROMACS](http://www.gromacs.org/)

Readers are welcome to submit their contributions for other hardware and software configurations.

## Run Benchmarks

1. Make sure cluster is properly configured and it is up and running

2. Clone the repository into the user home directory
    
    ```bash
    git clone git@github.com:Exabyte-io/exabyte-benchmarks.git
    ```

3. Install python virtualenv if you do not have it
    ```bash
    pip install virtualenv
    ```

4. Install required python packages

    ```bash
    cd exabyte-benchmarks
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    ```

5. Adjust [job.rms](job.rms) template as necessary.
    ```
    #!/bin/bash
     
    #PBS -N {{ NAME }}
    #PBS -j oe
    #PBS -R n
    #PBS -r n
    #PBS -q {{ QUEUE }}
    #PBS -l nodes={{ NODES }}
    #PBS -l ppn={{ PPN }}
    #PBS -l walltime={{ WALLTIME }}
    #PBS -m {{ NOTIFY }}
    #PBS -M {{ EMAIL }}
     
    module add {{ MODULE }}
    cd $PBS_O_WORKDIR
     
    # InfiniBand environment variables
    export I_MPI_FABRICS=shm:dapl
    export I_MPI_DAPL_PROVIDER=ofa-v2-cma-roe-enp94s0f0
    export I_MPI_DYNAMIC_CONNECTION=0
     
    start=`date +%s`
     
    {{ COMMAND }}
     
    end=`date +%s`
    echo $((end-start)) > {{ RUNTIME_FILE }}
    ```
    
    The above syntax is for PBS/Torque resource manager. 
    When needed, this file can be replaced to accomondate for other resource managers (ie. SLURM or LSF).

6. Set site name and location in [settings.py](settings.py). These settings are important to uniquely identify the sites.

7. Adjust modules and RMS settings in [settings.py](settings.py) as necessary, e.g set PPN to maximum number of cores per node.

8. Adjust HPL config in [hpl.json](cases/hpl.json). You can use the below links to generate the config
    - http://www.advancedclustering.com/act_kb/tune-hpl-dat-file
    - http://hpl-calculator.sourceforge.net/

9. Prepare the bechmark cases

    ```bash
        python run.py --prepare                              # prepares all cases
        python run.py --prepare --type hpl --type vasp       # prepares only hpl and vasp cases
        python run.py --prepare --name hpl-01 --name hpl-02  # prepares only hpl-{01,02} cases
    ```

10. Run the cases and waits for them to finish

    ```bash
        python run.py --execute                 # execute all cases
        python run.py --execute --type hpl      # execute only hpl cases
        python run.py --execute --name hpl-01   # execute only hpl-01 case
    ```

11. Store the results
    ```bash
        python run.py --results                 # store all results
        python run.py --results --type hpl      # store only hpl results
        python run.py --results --name hpl-01   # store only hpl-01 results
    ```

## Contribute

This is an open-source repository and we welcome contributions for other test cases. 
We suggest forking this repository and introducing the adjustments there. 
The changes in the fork can further be considered for merging into this repository as it is commonly used on Github. 
This process is explained in more details [here](https://gist.github.com/Chaser324/ce0505fbed06b947d962).

### How to add a new HPL case

1. Open [hpl.json](cases/hpl.json) file and add the HPL config for the new case.

### How to add a new VASP case

1. Put the POSCAR into the [POSCARS](benchmarks/vasp/POSCARS) directory or reuse existing ones

2. Put the INCAR into the [templates](benchmarks/vasp/templates) directory or reuse existing ones

3. Create a config as below and add it to the [CASES](cases/__init__.py).

    ```json
    {
        "name": "vasp-elb-01-04",
        "type": "vasp",
        "reference": "benchmarks.vasp.VASPCase",
        "config": {
            "nodes": 1,
            "ppn": 4,
            "kgrid": {
                "dimensions": [
                    1,
                    1,
                    1
                ],
                "shifts": [
                    0,
                    0,
                    0
                ]
            },
            "inputs": [
                {
                    "name": "INCAR",
                    "template": "benchmarks/vasp/templates/ELB-INCAR"
                },
                {
                    "name": "POSCAR",
                    "template": "benchmarks/vasp/POSCARS/Ba25Bi15O54"
                },
                {
                    "name": "KPOINTS",
                    "template": "benchmarks/vasp/templates/KPOINTS"
                }
            ],
            "pseudos": [
                "/export/share/pseudo/ba/gga/pbe/vasp/5.2/paw/sv/POTCAR",
                "/export/share/pseudo/bi/gga/pbe/vasp/5.2/paw/default/POTCAR",
                "/export/share/pseudo/o/gga/pbe/vasp/5.2/paw/default/POTCAR"
            ]
        }
    }
    ```

4. Adjust `inputs` according to step 1 and step 2.

5. Adjust The `pseudos` accordingly. It contains a list of pseudopotential absolute paths sorted by elements in INCAR file which will be concatenated together to form the POTCAR.

6. Adjust `kgrid` as necessary. The object is passed to `KPOINTS` template specified in `inputs` to create KPOINTS file. Adjust `KPOINTS` template or add new ones for extra parameters.

### How to add a new GROMACS case 

1. Put the tpr file into the [inputs](benchmarks/gromacs/inputs) directory or reuse existing ones

2. Create a config as below and add it to the [CASES](cases/__init__.py)

    ```json
    {
        "name": "model-1-01-04",
        "type": "gromacs",
        "reference": "benchmarks.gromacs.GROMACSCase",
        "config": {
            "nodes": 1,
            "ppn": 4,
            "inputs": [
                {
                    "name": "md.tpr",
                    "template": "benchmarks/gromacs/inputs/model-1/md.tpr"
                }
            ],
            "command": "source GMXRC.bash; mpirun -np $PBS_NP gmx_mpi_d mdrun -ntomp 1 -s md.tpr -deffnm md"
        }
    }
    ```

### Results Schema

The following shows the results schema.

```json
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "siteName": {
            "description": "Site name, e.g. AWS-NHT",
            "type": "string"
        },
        "siteLocation": {
            "description": "Site location, e.g. West Us",
            "type": "string"
        },
        "type": {
            "description": "Benchmark type, e.g. hpl",
            "type": "string"
        },
        "case": {
            "description": "Benchmark case, e.g. hpl-01",
            "type": "string"
        },
        "nodes": {
            "description": "Number of nodes used for the case",
            "type": "number"
        },
        "ppn": {
            "description": "Number of cores per node used for the case",
            "type": "number"
        },
        "runtime": {
            "description": "Benchmark runtime",
            "type": "number"
        },
        "memory": {
            "description": "Compute node total memory",
            "type": "number"
        },
        "cpuModel": {
            "description": "Compute node CPU model. e.g. Intel(R) Xeon(R) CPU E5-2666 v3 @ 2.90GHz",
            "type": "string"
        },
        "createdAt": {
            "description": "Benchmark creation time",
            "type": "string"
        }
    }
}
```
