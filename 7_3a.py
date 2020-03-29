#!/usr/bin/env python3
from sys import argv
inp_file = argv[1]
res_lst = []
xres_lst = []
res_dict = {}
with open(inp_file, 'r') as inp_fl:
    for line in inp_fl:
#        if 'DYNAMIC' in line:
#            res_lst.append(line.replace('DYNAMIC','')
        res_lst.append(line.lstrip(' ').strip('\n').replace('DYNAMIC','')) if 'DYNAMIC' in line else ''
#        print(line.lstrip(' ').strip('\n').replace('DYNAMIC','')) if 'DYNAMIC' in line else ''
        
#        print(line.replace('DYNAMIC','')) if 'DYNAMIC' in line else pass
for item in res_lst:
    xres_lst.append((item[:4],item[7:]))
print(xres_lst)
res_dict = dict(xres_lst)
for key in sorted(res_dict):
    print(key, res_dict[key])
#print(res_lst.sort(), sep = "\n")
