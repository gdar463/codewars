#!/bin/bash

cmake --build build -t UniqueOrder
if [ $? -eq 0 ]; then
    mv build/UniqueOrder build/uniqueOrder
    if [[ "${PWD}" != "/home/dario/projects/cpp/UniqueOrder" ]]; then
        cd UniqueOrder
    fi
    echo 
    ../build/uniqueOrder "${@:1}"
fi
