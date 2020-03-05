#!/usr/bin/env python3
ip_addr = input('Input ip address x.x.x.x:')
first_octet = ip_addr.split('.')[0]
if 1 < int(first_octet) and int(first_octet) < 223:
    print("Unicast")
elif 224 < int(first_octet) and int(first_octet) < 239:
    print("Multicast")
elif ip_addr == '255.255.255.255':
    print("local broadcast")
elif ip_addr == '0.0.0.0':
    print("Unassigned")
else:
    print("Unused")
