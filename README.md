# exabyte-benchmarks

This repository provides a set of tools to benchmark cloud provider and on-premise hardware.

## Usage

1. Make sure cluster is properly configured

2. Clone the repository into the user home directory
    
    ```bash
    git clone git@github.com:Exabyte-io/exabyte-test-cases.git
    ```

3. Install required python packages

    ```bash
    cd exabyte-test-cases
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    ```

4. Adjust modules and RMS settings in [settings.py](settings.py) as necessary

5. Adjust [job.rms](job.rms) template as necessary, e.g. to add IB environment variables

6. Adjust HPL config in [hpl.json](cases/hpl.json). You can use the below links to generate the config
    - http://www.advancedclustering.com/act_kb/tune-hpl-dat-file
    - http://hpl-calculator.sourceforge.net/

6. Prepare the cases

    ```bash
        python run.py --prepare    
    ```

7. Run the cases and waits for them to finish

    ```bash
        python run.py --execute
    ```

8. Get the results
    ```bash
        python run.py --results
    ```
