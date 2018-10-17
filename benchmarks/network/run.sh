#!/bin/bash

for DIR in `ls cases`; do
    cd cases/${DIR}
    sh run.sh
    cd -
done
