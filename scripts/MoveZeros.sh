#!/bin/bash

cmake --build build -t MoveZeros
if [ $? -eq 0 ]; then
    mv build/MoveZeros build/moveZeros
    if [[ "${PWD}" != "/home/dario/projects/cpp/MoveZeros" ]]; then
        cd MoveZeros
    fi
    echo 
    ../build/moveZeros "${@:1}"
fi
