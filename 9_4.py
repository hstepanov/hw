#!/usr/bin/env python3
#import pdb; pdb.set_trace()
from sys import argv
input_file = argv[1]


def convert_config_to_dict(config_name):
    
    ignore = ['duplex', 'alias', 'Current configuration']
    result_dct = {}

    def ignore_command(ignore, command):
        ''' check if item in ignore list exists in config command line'''
        for item in ignore: 
            if item in command:
                return True

    with open(config_name, 'r') as config:
        command_list = [line.rstrip() for line in config if '!' not in line]
#command_list = [
#    'interface Ethernet0/1',
#    ' switchport trunk encapsulation dot1q',
#    ' switchport trunk allowed vlan 100',
#    ' switchport mode trunk',
#    ' duplex auto',
#    ' spanning-tree portfast edge trunk'
#    ]
        cmd_index = 0
        cmd_index_local = 0
        for command in command_list:
            if ignore_command(ignore, command):
                cmd_index += 1
                pass
            elif not command.startswith(' '):
                result_dct.setdefault(command, [])
                cmd_index += 1
            elif command.startswith(' '):
                """if string starts with whitespace,
                then append it to the list of previous command"""
    #                print(result_dct[command_list[cmd_index]])
    #                print(result_dct[command_list[cmd_index - 1]])
                result_dct[command_list[cmd_index - 1]].append(command)
                cmd_index_local += 1
            
    return result_dct


print(convert_config_to_dict(input_file))
