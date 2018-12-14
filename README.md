# exabyte-test-cases

Runs a test case for structure readers and characteristic properties extraction, supported by exabyte.io.

## Usage

Control script run.py runs test cases based on the test input files and structures that are expected
to be in the directory provided as an argument.  Results of the test run will be available under `workdir` path.
Previously generated *.json files will be present next to the newly generated application results.

Example invocation:

```bash
python run.py characteristics/total_energy/espresso/FCC/
```

Application names (vasp, espresso) are read from the path.
