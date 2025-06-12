#!/bin/python3

import argparse
import os

parser = argparse.ArgumentParser("new codewars cpp project")
parser.add_argument("name")
parser.add_argument("-s", "--signature")
parser.add_argument("-o", "--official")
parser.add_argument("-l", "--link")

args = parser.parse_args()

project: str = args.name
projectLower = project[0].lower() + project[1:]

if args.signature is None:
    signature = input("Enter signature: ")
else:
    signature: str = args.signature

if args.official is None:
    official = input("Enter official name: ")
else:
    official: str = args.official

if args.link is None:
    link = input("Enter link: ")
else:
    link: str = args.link

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

template_string = '\t{{const}}{{type}} {{name}} = argv[{{index}}];'
inputs = ""
call = signature.split("(")[0].split(" ")[1] + "("
segments = signature.split("(")[1].split(")")[0].split(", ")
for i, val in enumerate(segments):
    temp = template_string if i != 0 else template_string.replace("\t", "")
    segment = val.split(" ")
    if "const" in segment:
        temp = temp.replace("{{const}}", "const ")
    temp = temp.replace("{{type}}", segment[0])
    temp = temp.replace("{{name}}", segment[-1].replace("&",""))
    call += segment[-1].replace("&", "") + (", " if i != len(segments) - 1 else "")
    temp = temp.replace("{{index}}", str(i)) + ("\n" if i != len(segments) - 1 else "")
    inputs += temp
call += ");"

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

with open(project + ".sh", "wt") as f:
    f.write(bashFile)

with open("CMakeLists.txt", "at") as f:
    f.write("add_executable(" + project + " " + project + "/main.cpp " + project + "/" + projectLower + ".cpp)\n")

os.makedirs(project)
with open(project + "/" + projectLower + ".cpp", "wt") as f:
    f.write(cppFile)
with open(project + "/main.cpp", "wt") as f:
    f.write(mainFile)
with open(project + "/README.md", "wt") as f:
    f.write(mdFile)

print("Done!")
