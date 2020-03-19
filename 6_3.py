#!/usr/bin/env python3
access_template = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]

access = {
    '0/12': '10',
    '0/14': '11',
    '0/16': '17',
    '0/17': '150'
}
trunk = {
        '0/1': ['add', '10', '20'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17']
    }

#for intf, vlan in access.items():
#    print('interface FastEthernet' + intf)
#    for command in access_template:
#        if command.endswith('access vlan'):
#            print(' {} {}'.format(command, vlan))
#        else:
#            print(' {}'.format(command))
for intf, value in trunk.items():
    print('interface FastEthernet' + intf)
    for command in trunk_template:
        if 'add' in value and 'allowed' in command:
            print(' {} {}'.format(command, ','.join([str(x) for x in value])))

        elif 'only' in value and 'allowed' in command:
            print(' {} {}'.format(command, ','.join([str(x) for x in value[1:]])))

        elif 'del' in value and 'allowed' in command:
            print(' {} {}'.format(command, str(value[-1])))
        else:
            print(' {}'.format(command))
#    #    print(intf, '-->', value)
