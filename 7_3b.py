#!/usr/bin/env python3
# script read data from stdin (cam_table.txt and vlan number), sort data by vlan-number and print it
from sys import argv
inp_file = argv[1]
inp_vlan = int(argv[2])
res_lst = []
with open(inp_file, 'r') as inp_fl:
    for line in inp_fl:
        if 'DYNAMIC' in line: 
            x = line.lstrip(' ').strip('\n').replace('DYNAMIC','')
            res_lst.append(x.split(' '))

for item in res_lst:
    item[0] = int(item[0])
res_lst.sort()
for item in res_lst:
    if inp_vlan in item:
        if item[0] < 100:
            print('{}    {}  {}'.format(item[0], item[5], item[-1]))
        elif item[0] < 1000:
            print('{}   {}  {}'.format(item[0], item[4], item[-1]))
        elif item[0] > 999:
            print('{}  {}  {}'.format(item[0], item[3], item[-1]))
