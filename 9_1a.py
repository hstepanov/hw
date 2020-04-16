#!/usr/bin/env python3
access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

port_security_template = [
    'switchport port-security maximum 2',
    'switchport port-security violation restrict',
    'switchport port-security'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}

if len(port_security_template) > 0:
    print('OK')
else:
    print('NOT OK')

def gen_config(access_mode_template, access_config, *args):
    config = []
    for intf, vlan in access_config.items():
        config.append(print('interface {}'.format(intf)))
        for command in access_mode_template:
            if command.endswith('vlan'):
                config.append(print(command, vlan))
            else:
                config.append(print(command))
        for command in port_security_template:
            config.append(print(command))
#        if len(port_security_template) > 0:
#            print('OK')
#        else:
#            print('NOT OK')
    return config
gen_config(access_mode_template, access_config)
#        port_security_template)
