#!/usr/bin/env python3

import argparse
import os
from sys import platform
from lib import sort_out_stuff, replace_by_dir

parser = argparse.ArgumentParser("new codewars cpp project")
parser.add_argument("name")
parser.add_argument("-s", "--signature")
parser.add_argument("-o", "--official")
parser.add_argument("-l", "--link")

args = parser.parse_args()

project: str = args.name
projectLower = project[0].lower() + project[1:]

def get_if_not_passed(arg_name: str, name: str | None = None):
    if vars(args)[arg_name] is None:
        if name is None:
            return input("Enter " + arg_name + ": ")
        return input("Enter " + name + ": ")
    return str(vars(args)[arg_name])

signature = get_if_not_passed("signature")
official = get_if_not_passed("official", "official name")
link = get_if_not_passed("link")

imports = ""
needs_import = {
    "std::string": "<string>",
    "std::list": "<list>",
    "std::map": "<map>",
    "std::array": "<array>",
    "std::set": "<set>",
    "std::vector": "<vector>"
}
for key, val in needs_import.items():
    if signature.find(key) != -1:
        imports = imports + "#include " + val + "\n"

needs_replace = {
    "unsigned int": "uint",
    "long long": "longlong",
    "unsigned long long": "ulonglong"
}
needs_wrapper = {
    "int": tuple(["std::atoi(", ")"]),
    "long": tuple(["std::atol(", ")"]),
    "long long": tuple(["std::atoll(", ")"]),
    "unsigned long long": tuple(["std::stoull(",")"]),
    "double": tuple(["std::atof(", ")"])
}

inputs, call, imports = sort_out_stuff(signature, needs_wrapper, needs_replace, imports)

bashFileReplacements = {
    "{{projectName}}": project,
    "{{projectFile}}": projectLower
}
with open("example/example.sh", "rt") as f:
    bashFile = f.read()
bashFile = replace_by_dir(bashFile, bashFileReplacements)

cppFileReplacements = {
    "{{project}}": project,
    "{{signature}}": signature,
    "{{imports}}": imports
}
with open("example/example.cpp", "rt") as f:
    cppFile = f.read()
cppFile = replace_by_dir(cppFile, cppFileReplacements)

mainFileReplacements = {
    "{{imports}}": imports,
    "{{signature}}": signature + ";",
    "{{inputs}}": inputs,
    "{{call}}": call
}
with open("example/main.cpp", "rt") as f:
    mainFile = f.read()
mainFile = replace_by_dir(mainFile, mainFileReplacements)

mdFileReplacements= {
    "{{projectName}}": project,
    "{{officialName}}": official,
    "{{link}}": link,
}
with open("example/README.md", "rt") as f:
    mdFile = f.read()
mdFile = replace_by_dir(mdFile, mdFileReplacements)

with open("scripts/" + project + ".sh", "wt") as f:
    f.write(bashFile)
if platform == "linux":
    os.system("chmod +x ./scripts/" + project + ".sh")

with open("CMakeLists.txt", "at") as f:
    f.write("add_executable(" + project + " " + project + "/main.cpp " + project + "/" + projectLower + ".cpp)\n")

os.makedirs(project)
with open(project + "/" + projectLower + ".cpp", "wt") as f:
    f.write(cppFile)
with open(project + "/main.cpp", "wt") as f:
    f.write(mainFile)
with open(project + "/README.md", "wt") as f:
    f.write(mdFile)

os.system("cd build; cmake ..")

print("Done!")
