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

        for command in command_list:
            if ignore_command(ignore, command):
                pass
            elif not command.startswith(' '):
                result_dct.setdefault(command, [])
#            if string starts with whitespace,
#            then remove whitespace in the beginnning
#            and append it to the list of previous command
            elif command.startswith(' '):
                list(result_dct.values())[-1].append(command.lstrip())

    return result_dct

print(convert_config_to_dict(input_file))
