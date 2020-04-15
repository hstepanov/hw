#!/usr/bin/env python3
access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}

def gen_config(access_mode_template, access_config):
    config = []
    for intf, vlan in access_config.items():
        config.append(print('interface {}'.format(intf)))
        for command in access_mode_template:
            if command.endswith('vlan'):
                config.append(print(command, vlan))
            else:
                config.append(print(command))
    return config
gen_config(access_mode_template, access_config)
