#!/bin/bash

cmake --build build -t BitCount
if [ $? -eq 0 ]; then
    mv build/BitCount build/bitCount
    if [[ "${PWD}" != "/home/dario/projects/cpp/BitCount" ]]; then
        cd BitCount
    fi
    echo 
    ../build/bitCount "${@:1}"
fi
