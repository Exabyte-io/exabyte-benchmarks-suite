# Exabyte Benchmarks Suite (ExaBench)

This repository provides a command-line tool (`exabench`) to benchmark hardware for distributed computing.

We use this tool to benchmark cloud provider systems for the cases supported below, relevant for materials modeling:

- High-performance Linpack ([HPL](http://www.netlib.org/benchmark/hpl/))
- [Vienna ab-initio simulations provider](https://www.vasp.at/)
- [GROMACS](http://www.gromacs.org/)

More information about the test cases per each application, including the input sources, is provided inside their corresponding directories.

The latest benchmark results are maintained at this [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1oBHR8bp9q86MOxGYXcvUWHZa8KiC-uc_qX-UF1iqf-Y/edit). 
Please note that the data stored there is preliminary/raw and so might not be accurate.

Readers are welcome to submit their contributions for other hardware and software configurations following the guidelines in the [Contribution](#contribution) section below.

## Requirements

It is assumed that the benchmarks are executed on a computing cluster containing a resource management system (RMS) such as Torque/PBS (supported by default). In order to support other RMS such as SLURM or LSF, users can follow the explanation in [Configuration](#configuration) section below.

By default, [Environment Modules](http://modules.sourceforge.net/) are used to load the software applications needed by the benchmarks.
Follow the explanation in [Configuration](#configuration) section below for systems where Environment Modules are not available.

## Installation

1. Install [git-lfs](https://help.github.com/articles/installing-git-large-file-storage/) in order to get files stored on git LFS.

2. Clone the repository into the user home directory
    ```bash
    git clone git@github.com:Exabyte-io/exabyte-benchmarks.git
    ```

3. Install python virtualenv if it is not installed
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

5. Add `exabench` command to `PATH`

    ```bash
    export PATH=`pwd`:${PATH}
    ```

## Configuration

1. Adjust [job.rms](job.rms) template as necessary. Please note that the template is for PBS/Torque.
In order to incorporate support for other resource managers one should adjust the RMS directives (`#PBS`) accordingly.

2. Set site name and location in [settings.py](settings.py). These settings are important to uniquely identify the sites.

3. Adjust RMS settings in [settings.py](settings.py) as necessary, e.g set PPN to maximum number of cores per node.

4. Adjust `MODULES` settings in [settings.py](settings.py) to load the software applications needed by the benchmarks.
If Environment Modules are not installed, one should adjust the `command` inside benchmark configs to load required libraries.

5. Adjust [HPL configs](benchmarks/hpl/cases.json). Use the below links to generate the initial configs.
    - http://www.advancedclustering.com/act_kb/tune-hpl-dat-file
    - http://hpl-calculator.sourceforge.net/


## Execution

1. Prepare the benchmark cases. This creates cases directories, job script files and cases input files.
    ```bash
        exabench --prepare                              # prepares all cases
        exabench --prepare --type hpl --type vasp       # prepares only hpl and vasp cases
        exabench --prepare --name hpl-01 --name hpl-02  # prepares only hpl-{01,02} cases
    ```

2. Run the cases and wait for them to finish. Use `qstat` command to monitor the progress if available.
    ```bash
        exabench --execute                 # execute all cases
        exabench --execute --type hpl      # execute only hpl cases
        exabench --execute --name hpl-01   # execute only hpl-01 case
    ```

3. Store and publish the results
    ```bash
        exabench --results                 # store all results
        exabench --results --type hpl      # store only hpl results
        exabench --results --name hpl-01   # store only hpl-01 results
    ```

4. Plot the results
    ```bash
        exabench --plot --metric PerformancePerCore  # compare all sites
        exabench --plot --metric SpeedupRatio --site-name AWS-NHT --site-name AZURE-IB-H  # compare given sites
    ```

### Results

Benchmark results are stored in the [local cache](results/results.json) and are also published to this [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1oBHR8bp9q86MOxGYXcvUWHZa8KiC-uc_qX-UF1iqf-Y/edit) with the format specified in the [schema](results/schema.json) file (one-level dictionary with no nested keys). 
Set `PUBLISH_RESULTS` to `False` in [settings.py](settings.py) to disable publishing results to Google Spreadsheet. 

## Contribution

This is an open-source repository and we welcome contributions for other test cases.
We suggest forking this repository and introducing the adjustments there.
The changes in the fork can further be considered for merging into this repository as it is commonly used on Github.
This process is explained in more details [here](https://gist.github.com/Chaser324/ce0505fbed06b947d962).

### Adding New Cases

This section explains how to add new benchmark cases.

#### HPL

1. Open [HPL cases](benchmarks/hpl/cases.json) file and add the HPL config for the new case.

#### VASP

1. Put the POSCAR into the [POSCARS](benchmarks/vasp/POSCARS) directory or reuse existing ones

2. Put the INCAR into the [templates](benchmarks/vasp/templates) directory or reuse existing ones

3. Create a config as below and add it to [VASP CASES](benchmarks/vasp/cases.py).

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

#### GROMACS

1. Put the tpr file into the [inputs](benchmarks/gromacs/inputs) directory or reuse existing ones

2. Create a config as below and add it to [GROMACS CASES](benchmarks/gromacs/cases.py)

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

### New Metrics

1. Create a class inside [metrics](metrics) package and inherit it from base [Metric](metrics/__init__.py) class, e.g. [PerformancePerCore](metrics/performance_per_core.py).

2. Implement `config` and `plot` methods accordingly.

3. Register the new metric inside [METRICS_REGISTRY](settings.py).
