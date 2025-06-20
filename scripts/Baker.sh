#!/bin/bash

cmake --build build -t Baker
if [ $? -eq 0 ]; then
    mv build/Baker build/baker
    if [[ "${PWD}" != "/home/dario/projects/cpp/Baker" ]]; then
        cd Baker
    fi
    echo 
    ../build/baker "${@:1}"
fi
