#!/bin/bash

cmake --build build -t Alphabet
if [ $? -eq 0 ]; then
    mv build/Alphabet build/alphabet
    if [[ "${PWD}" != "/home/dario/projects/cpp/Alphabet" ]]; then
        cd Alphabet
    fi
    echo 
    ../build/alphabet "${@:1}"
fi
