#!/bin/bash

cmake --build build -t {{projectName}}
if [ $? -eq 0 ]; then
    mv build/{{projectName}} build/{{projectFile}}
    if [[ "${PWD}" != "/home/dario/projects/cpp/{{projectName}}" ]]; then
        cd {{projectName}}
    fi
    echo 
    ../build/{{projectFile}}
fi
