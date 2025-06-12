#!/bin/bash

cmake --build build -t StringEnds
if [ $? -eq 0 ]; then
    mv build/StringEnds build/stringEnds
    if [[ "${PWD}" != "/home/dario/projects/cpp/StringEnds" ]]; then
        cd StringEnds
    fi
    echo 
    ../build/stringEnds
fi
