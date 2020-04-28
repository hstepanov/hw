#!/usr/bin/env python3
from sys import argv
input_file = argv[1]

def convert_config_to_dict(config_name):
    
    ignore = ['duplex', 'alias', 'Current configuration']
    result_dict = {}

    def ignore_command(command,ignore):
        if command in ignore:
            return True
        else:
            return False

    with open(config_name, 'r') as config:
        command_list = [line.rstrip() for line in config if '!' not in line]
        '''print(command_list)'''
        for command in command_list:
            if ignore_command(command, ignore):
                pass
            else:
                print(command)
                result_dict[command] = []
            '''if not ignore_command(command,ignore) and not command.startswith(' '):
                print(command)'''

    return result_dict



print(convert_config_to_dict(input_file))
