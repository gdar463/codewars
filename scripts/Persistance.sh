#!/bin/bash

cmake --build build -t Persistance
if [ $? -eq 0 ]; then
    mv build/Persistance build/persistance
    if [[ "${PWD}" != "/home/dario/projects/cpp/Persistance" ]]; then
        cd Persistance
    fi
    echo 
    ../build/persistance "${@:1}"
fi
