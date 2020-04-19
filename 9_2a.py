#!/usr/bin/env python3
trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

def conf_gen(trunk_mode_template, trunk_config):
    ports_list = []
    for port in trunk_config:
        ports_list.append(port)
    result_dict = dict.fromkeys(ports_list, [])

    for port,vlan in trunk_config.items():
        command_list = []
        for command in trunk_mode_template:
            if command.endswith('vlan'):
                command_list.append('{} {}'.format(command,','.join(map(str,vlan))))
            else:
                command_list.append(command)
        result_dict[port] = command_list
    return print(result_dict)
conf_gen(trunk_mode_template, trunk_config)
