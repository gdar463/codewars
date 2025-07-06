#!/usr/bin/env python3

import argparse
import os
from sys import platform
import sys
from lib import sort_out_stuff, replace_by_dir

parser = argparse.ArgumentParser("Codewars CPP Setup", description="Creates a new CMake target for developing Katas locally")
parser.add_argument("name", help="Name of the project (use for folder and file name)")
parser.add_argument("-s", "--signature", help="Signature of the function given by the Kata")
parser.add_argument("-o", "--official", help="Official name of the Kata")
parser.add_argument("-l", "--link", help="Link to the Kata")
parser.add_argument("--dry-run", help="Don't write files", action="store_true")
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit()

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
dry_run: bool = args.dry_run if vars(args)["dry_run"] is not None else False

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

return_type = signature.split(" ")[0]
isVector = False
vectorType = ""
if "vector" in return_type:
    isVector = True
    vectorType = return_type.split("<")[1].split(">")[0]

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

mainFile = ""
mainFileReplacements = {
    "{{imports}}": imports,
    "{{signature}}": signature + ";",
    "{{inputs}}": inputs,
    "{{call}}": call
}
if isVector:
    mainFileReplacements = mainFileReplacements | {
        "{{type}}": vectorType
    }
    with open("example/mainVector.cpp", "rt") as f:
        mainFile = f.read()
else:
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

if not dry_run:
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
else:
    print("-- Bash File: \"scripts/" + project + ".sh\"\n")
    print("```")
    print(bashFile, end="")
    print("```\n")

    print("-- CMake Line:\n")
    print("```")
    print("add_executable(" + project + " " + project + "/main.cpp " + project + "/" + projectLower + ".cpp)")
    print("```\n")
    
    print("-- CPP File: \"" + project + "/" + projectLower + ".cpp\"\n")
    print("```")
    print(cppFile, end="")
    print("```\n")
    print("-- Main File: \"" + project + "/main.cpp\"\n")
    print("```")
    print(mainFile, end="")
    print("```\n")
    print("-- README File: \"" + project + "/README.md\"\n")
    print("```")
    print(mdFile, end="")
    print("```\n")

print("Done!")
