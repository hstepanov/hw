#!/usr/bin/env python3
from sys import argv
file_name = argv[1]
ignore = ['duplex', 'alias', 'Current configuration']
with open( file_name, 'r') as fl:
    for line in fl:
        line.rstrip('\n')
        if '!' in line or ignore[0] in line or ignore[1] in line or ignore[2] in line :
            pass
        else:
            print(line.strip('\n'))

