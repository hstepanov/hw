#!/usr/bin/env python3
from sys import argv
inp_file = argv[1]
with open(inp_file, 'r') as inp_fl:
    for line in inp_fl:
        if 'DYNAMIC' in line:
            print(line[0:26],line[33:])
