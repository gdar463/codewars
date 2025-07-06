#!/usr/bin/env python3

def replace_by_dir(input: str, replacement_patterns: dict[str, str]):
    for pattern, replace in replacement_patterns.items():
        input = input.replace(pattern,replace)
    return input

def sort_out_stuff(signature: str, needs_wrapper: dict[str, tuple[str, ...]], needs_replace: dict[str,str], imports: str):
    def replace_types(input: str): 
        for official, temp_name in needs_replace.items():
            input = input.replace(official, temp_name)
        return input

    def replace_types_inv(input:str):
        for official, temp_name in needs_replace.items():
            input = input.replace(temp_name, official)
        return input

    template_string = '{{const}}{{type}} {{name}}{{wrapperStart}}argv{{index}}{{wrapperEnd}};'
    inputs = "\t"
    call = signature.split("(")[0].split(" ")[1] + "("
    segments = signature.split("(")[1].split(")")[0].split(", ")
    for i, val in enumerate(segments):
        temp = template_string
        segment = replace_types(val).split(" ")
        zero_inv = replace_types_inv(segment[0])

        if zero_inv in needs_wrapper:
            wrapper = needs_wrapper[zero_inv]
            if segment[0].count("ulonglong") > 0:
                imports = imports + "#include <string>\n"
        else:
            wrapper = tuple(["",""])
            
        tempReplacements = {
            "{{const}}": "const " if "const" in segment else "",
            "{{type}}": replace_types_inv(segment[1]) if "const" in segment else zero_inv,
            "{{name}}": segment[-1].replace("&", ""),
            "{{wrapperStart}}": wrapper[0],
            "{{wrapperEnd}}": wrapper[1],
            "{{index}}": "[" + str(i + 1) + "]" if "vector" not in zero_inv.split("<")[0] else ""
        }
        
        call += segment[-1].replace("&", "") + (", " if i != len(segments) - 1 else "")
        temp = replace_by_dir(temp, tempReplacements) + ("\n" if i != len(segments) - 1 else "")
        inputs += temp
    call += ")"
    return inputs, call, imports
