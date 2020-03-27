#!/usr/bin/env python3
# script read text from config-file and write result in config_cleared.txt
from sys import argv
file_name = argv[1]
ignore = ['duplex', 'alias', 'Current configuration']
with open( file_name, 'r') as fl, open('config_sw1_cleared.txt', 'a') as result_file:
    for line in fl:
        line.rstrip('\n')
        if ignore[0] in line or ignore[1] in line or ignore[2] in line :
            pass
        else:
            result_file.write(line)

