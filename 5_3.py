#!/usr/bin/env python3
interface_mode = input('Input interface mode (access/trunk):')
interface = input('Input interface:')
vlan = input('Input vlan(s) number:')
access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
print('\ninterface {}'.format(interface))
if interface_mode == 'access':
    print('\n'.join(access_template).format(vlan))
else:
    print('\n'.join(trunk_template).format(vlan))
