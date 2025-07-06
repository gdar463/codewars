#!/bin/bash

cmake --build build -t Smileys
if [ $? -eq 0 ]; then
    mv build/Smileys build/smileys
    if [[ "${PWD}" != "/home/dario/projects/cpp/Smileys" ]]; then
        cd Smileys
    fi
    echo 
    ../build/smileys "${@:1}"
fi
