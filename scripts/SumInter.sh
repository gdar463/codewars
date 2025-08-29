#!/bin/bash

cmake --build build -t SumInter
if [ $? -eq 0 ]; then
    mv build/SumInter build/sumInter
    if [[ "${PWD}" != "/home/dario/projects/cpp/SumInter" ]]; then
        cd SumInter
    fi
    echo 
    ../build/sumInter "${@:1}"
fi
