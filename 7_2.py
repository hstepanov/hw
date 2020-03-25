#!/usr/bin/env python3
from sys import argv
file_name = argv[1]
with open( file_name, 'r') as fl:
    for line in fl:
        line.rstrip('\n')
        if '!' in line:
            pass
        else:
            print(line.strip('\n'))

