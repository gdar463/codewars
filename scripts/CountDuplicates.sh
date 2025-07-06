#!/bin/bash

cmake --build build -t CountDuplicates
if [ $? -eq 0 ]; then
    mv build/CountDuplicates build/countDuplicates
    if [[ "${PWD}" != "/home/dario/projects/cpp/CountDuplicates" ]]; then
        cd CountDuplicates
    fi
    echo 
    ../build/countDuplicates "${@:1}"
fi
