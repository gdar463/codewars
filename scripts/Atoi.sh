#!/bin/bash

cmake --build build -t Atoi
if [ $? -eq 0 ]; then
    mv build/Atoi build/atoi
    if [[ "${PWD}" != "/home/dario/projects/cpp/Atoi" ]]; then
        cd Atoi
    fi
    echo 
    ../build/atoi "${@:1}"
fi
