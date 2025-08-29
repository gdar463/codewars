#!/bin/bash

cmake --build build -t GetPINs
if [ $? -eq 0 ]; then
    mv build/GetPINs build/getPINs
    if [[ "${PWD}" != "/home/dario/projects/cpp/GetPINs" ]]; then
        cd GetPINs
    fi
    echo 
    ../build/getPINs "${@:1}"
fi
