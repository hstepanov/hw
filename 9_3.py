#!/usr/bin/env python3
# script should return tuple of 2 dicts (access_dict and trunk_dict)
from sys import argv
input_file = argv[1]

def get_int_vlan_map(input_file):
    access_dict = {}
    trunk_dict = {}
    with open(input_file, 'r') as inp_f:
        for line in inp_f:
            if 'Ethernet' in line:
                interface = line.split()[-1]
            elif 'switchport access' in line:
                access_vlan = line.split()[-1]
                access_dict[interface] = access_vlan
            elif 'switchport trunk allowed' in line:
                trunk_vlan_list = line[31:].rstrip().split(',')
                trunk_dict[interface] = trunk_vlan_list
    return (access_dict, trunk_dict)
print(get_int_vlan_map(input_file))

