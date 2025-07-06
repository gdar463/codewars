#!/bin/bash

cmake --build build -t CamelCase
if [ $? -eq 0 ]; then
    mv build/CamelCase build/camelCase
    if [[ "${PWD}" != "/home/dario/projects/cpp/CamelCase" ]]; then
        cd CamelCase
    fi
    echo 
    ../build/camelCase "${@:1}"
fi
