#!/usr/bin/env python3
# script read data from cam_table.txt and print sorted data by vlan-number
from sys import argv
inp_file = argv[1]
res_lst = []
xres_lst = []
res_dict = {}
with open(inp_file, 'r') as inp_fl:
    for line in inp_fl:
        if 'DYNAMIC' in line: 
            x = line.lstrip(' ').strip('\n').replace('DYNAMIC','')
            res_lst.append(x.split(' '))

for item in res_lst:
    item[0] = int(item[0])
res_lst.sort()
for item in res_lst:
    if item[0] < 100:
        print('{}    {}  {}'.format(item[0], item[5], item[-1]))
    elif item[0] < 1000:
        print('{}   {}  {}'.format(item[0], item[4], item[-1]))
    else:
        print('{}  {}  {}'.format(item[0], item[3], item[-1]))
