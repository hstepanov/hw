#!/usr/bin/env python3
from sys import argv
input_file = argv[1]

def get_int_vlan_map(input_file):
    access_dict = {}
    trunk_dict = {}
    with open(input_file, 'r') as inp_f:
        for line in inp_f:
            if 'Ethernet' in line:
                interface = line.split()[-1]
                print(interface)
            elif 'switchport access' in line:
                access_vlan = line.split()[-1]
                print(access_vlan)
            elif 'switchport trunk allowed' in line:
                trunk_vlan_list = line[31:]
                print(trunk_vlan_list.rstrip().split(','))

get_int_vlan_map(input_file)

