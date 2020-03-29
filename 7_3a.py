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
#       res_lst.append(line.lstrip(' ').strip('\n').replace('DYNAMIC','')) if 'DYNAMIC' in line else ''
        if 'DYNAMIC' in line: 
            x = line.lstrip(' ').strip('\n').replace('DYNAMIC','')
            res_lst.append(x.split(' '))

for item in res_lst:
    print(item)
#        print(line.lstrip(' ').strip('\n').replace('DYNAMIC','')) if 'DYNAMIC' in line else ''
        
#        print(line.replace('DYNAMIC','')) if 'DYNAMIC' in line else pass

#for item in res_lst:
#    xres_lst.append((item[-5:],item[:-5]))
#res_dict = dict(xres_lst)
#for key,value in sorted(res_dict.items()):
#    print(value, key)
#print(res_lst.sort(), sep = "\n")
