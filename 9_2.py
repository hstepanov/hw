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
    result = []
    for port, vlan in trunk_config.items():
        result.append('{} {}'.format('interface',port))
        for command in trunk_mode_template:
            if command.endswith('vlan'):
                result.append('{} {}'.format(command,','.join(map(str,vlan))))
            else:
                result.append(command)
    return print(result)
conf_gen(trunk_mode_template, trunk_config)
