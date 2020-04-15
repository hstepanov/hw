#!/usr/bin/env python3
# script accept cam_table.txt, as input file and print vlan, mac and port on stdout
from sys import argv
inp_file = argv[1]
with open(inp_file, 'r') as inp_fl:
    for line in inp_fl:
        if 'DYNAMIC' in line:
#            print(line[0:26],line[33:])
            vlan, mac, typee, port = line.split()
            print(f"{vlan.strip(' '):<6} {mac:<18} {port}")
