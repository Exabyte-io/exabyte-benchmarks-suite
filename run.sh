#!/bin/bash

for DIR in `ls benchmarks`; do
    cd benchmarks/${DIR}
    sh run.sh
    cd -
done
