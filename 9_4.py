#!/usr/bin/env python3
from sys import argv
input_file = argv[1]

def convert_config_to_dict(config_name):
    
    ignore = ['duplex', 'alias', 'Current configuration']
    result_dict = {}

    def ignore_command(command,ignore):
        if command not in ignore:
            return True
        else:
            return False

    with open(config_name, 'r') as config:
        command_list = [line.rstrip() for line in config if '!' not in line]
        print(command_list)
        for command in command_list:
            if not ignore_command(command,ignore) and not command.startswith(' '):
                print(command)
                result_dict[command] = []

    return print(result_dict)



convert_config_to_dict(input_file)
