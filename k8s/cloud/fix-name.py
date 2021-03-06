#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Replace PROJECT_ID & TODOAPI_IP_ADDR with real values for *.yml.tpl files.

   e.g., 
     gcr.io/PROJECT_ID/todoapi        --> gcr.io/my_proj/todoapi
     loadBalancerIP: TODOAPI_IP_ADDR  --> loadBalancerIP: 140.113.23.100
"""


import shutil
from tempfile import mkstemp

def sed(pattern, replace: str, source: str, dest: str = None, count: int = 0) -> int:
    """Reads a source file and writes the destination file.

    In each line, replaces pattern with replace.

    Args:
        pattern (str): pattern to match (can be re.pattern)
        replace (str): replacement str
        source  (str): input filename
        count (int): number of occurrences to replace; 0 means unlimited.
        dest (str):   destination filename, if not given, source will be over written.

    Returns:
        int: total number of replacement

    @see https://stackoverflow.com/a/40843600/714426        
    """

    fin = open(source, 'r')
    num_replaced = 0

    if dest:
        fout = open(dest, 'w')
    else:
        _, name = mkstemp()
        fout = open(name, 'w')

    for line in fin:
        out = re.sub(pattern, replace, line)
        fout.write(out)

        if out != line:
            num_replaced += 1
        if count and num_replaced > count:
            break
    try:
        fout.writelines(fin.readlines())
    except Exception as E:
        raise E

    fin.close()
    fout.close()

    if not dest:
        shutil.move(name, source)

    return num_replaced


import glob, os, re, sys

if __name__ == '__main__':

    if len(sys.argv) < 2:
        raise Exception('missing PROJECT_ID & TODOAPI_IP_ADDR as arguments.')

    if len(sys.argv) < 3:
        raise Exception('missing TODOAPI_IP_ADDR as 2nd argument.')

    project_id = sys.argv[1]
    todoapi_host = sys.argv[2]

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("Replacing *.yml.tpl & *.yaml.tpl files in %s..." % dir_path)

    yml_tpl_files  = glob.glob(os.path.join(dir_path, "*.yml.tpl"))
    yaml_tpl_files = glob.glob(os.path.join(dir_path, "*.yaml.tpl"))

    for filename in [*yml_tpl_files, *yaml_tpl_files]:
        #print(filename)
        searchObj = re.search( r'(.+)\.tpl', filename, re.M|re.I)
        if searchObj:
            #print ("searchObj.group() : ", searchObj.group())
            new_filename = searchObj.group(1)
            print(" > %s -> %s" % (os.path.basename(filename), os.path.basename(new_filename)))

            sed("PROJECT_ID", project_id, filename, new_filename)
            sed("TODOAPI_IP_ADDR", todoapi_host, new_filename)
            print("   Done.")