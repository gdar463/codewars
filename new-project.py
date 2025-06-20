#!/bin/python3

import argparse
import os
from sys import platform

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

needs_wrapper = {
    "int": tuple(["std::atoi(", ")"]),
    "long": tuple(["std::atol(", ")"]),
    "long long": tuple(["std::atoll(", ")"]),
    "unsigned long long": tuple(["std::stoull(",")"]),
    "double": tuple(["std::atof(", ")"])
}

template_string = '\t{{const}}{{type}} {{name}} = {{wrapperStart}}argv[{{index}}]{{wrapperEnd}};'
inputs = ""
call = signature.split("(")[0].split(" ")[1] + "("
segments = signature.split("(")[1].split(")")[0].split(", ")
for i, val in enumerate(segments):
    temp = template_string if i != 0 else template_string.replace("\t", "")
    segment = val.replace("unsigned int","uint").replace("unsigned long long", "ulonglong").replace("long long", "longlong").split(" ")
    temp = temp.replace("{{const}}", "const " if "const" in segment else "")
    temp = temp.replace("{{type}}", segment[1 if "const" in segment else 0].replace("uint", "unsigned int").replace("ulonglong", "unsigned long long").replace("longlong", "long long"))
    temp = temp.replace("{{name}}", segment[-1].replace("&",""))
    if segment[0].replace("uint", "unsigned int").replace("ulonglong", "unsigned long long").replace("longlong", "long long") in needs_wrapper:
        wrapper = needs_wrapper[segment[0].replace("uint", "unsigned int").replace("ulonglong", "unsigned long long").replace("longlong", "long long")]
        if segment[0].count("ulonglong") > 0:
            imports = imports + "#include <string>\n"
    else:
        wrapper = tuple(["",""])
    temp = temp.replace("{{wrapperStart}}", wrapper[0])
    temp = temp.replace("{{wrapperEnd}}", wrapper[1])
    call += segment[-1].replace("&", "") + (", " if i != len(segments) - 1 else "")
    temp = temp.replace("{{index}}", str(i + 1)) + ("\n" if i != len(segments) - 1 else "")
    inputs += temp
call += ")"

with open("example/example.sh", "rt") as f:
    bashFile = f.read()
bashFile = bashFile.replace("{{projectName}}", project)
bashFile = bashFile.replace("{{projectFile}}", projectLower)

with open("example/example.cpp", "rt") as f:
    cppFile = f.read()
cppFile = cppFile.replace("{{project}}", project)
cppFile = cppFile.replace("{{signature}}", signature)
cppFile = cppFile.replace("{{imports}}", imports)

with open("example/main.cpp", "rt") as f:
    mainFile = f.read()
mainFile = mainFile.replace("{{imports}}", imports)
mainFile = mainFile.replace("{{signature}}", signature + ";")
mainFile = mainFile.replace("{{inputs}}", inputs)
mainFile = mainFile.replace("{{call}}", call)

with open("example/README.md", "rt") as f:
    mdFile = f.read()
mdFile = mdFile.replace("{{projectName}}", project)
mdFile = mdFile.replace("{{officialName}}", official)
mdFile = mdFile.replace("{{link}}", link)

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
