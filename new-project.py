#!/bin/python3

import os
import sys

if (len(sys.argv) > 1):
    project = sys.argv[1]
else:
    project = input("Enter project name: ")
projectUpper = project[0].upper() + project[1:]

with open("example/example.sh", "rt") as f:
    bashFile = f.read()
bashFile = bashFile.replace("{{projectName}}", projectUpper)
bashFile = bashFile.replace("{{projectFile}}", project)

with open("example/example.cpp", "rt") as f:
    cppFile = f.read()
cppFile = cppFile.replace("{{project}}", projectUpper)

with open(project + ".sh", "wt") as f:
    f.write(bashFile) # pyright: ignore[reportUnusedCallResult]

with open("CMakeLists.txt", "at") as f:
    f.write("add_executable(" + projectUpper + " " + projectUpper + "/" + project + ".cpp)\n") # pyright: ignore[reportUnusedCallResult]

os.makedirs(projectUpper)
with open(projectUpper + "/" + project + ".cpp", "wt") as f:
    f.write(cppFile) # pyright: ignore[reportUnusedCallResult]

print("Done!")
