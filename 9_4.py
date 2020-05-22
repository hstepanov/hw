#!/usr/bin/env python3
#import pdb; pdb.set_trace()
from sys import argv
input_file = argv[1]

def convert_config_to_dict(config_name):
    
    ignore = ['duplex', 'alias', 'Current configuration']
    result_dict = {}

    def ignore_command(ignore, command):
        ''' check if item in ignore list exists in config command line'''
        for item in ignore: 
            if item in command:
                return True
#            else:
#                return False
    

    with open(config_name, 'r') as config:
        command_list = [line.rstrip() for line in config if '!' not in line]
        cmd_index = 0
        cmd_local_index = 0
        for command in command_list:
            if ignore_command(ignore, command):
                cmd_index += 1
                pass
            elif not command.startswith(' '):
                result_dict[command] = []
                cmd_index += 1
            elif command.startswith(' '):
                result_dict.setdefault(command_list[cmd_index], []).append(command)
                cmd_local_index += 1
            else:
                cmd_index = cmd_local_index + 1
            
    return result_dict



print(convert_config_to_dict(input_file))
