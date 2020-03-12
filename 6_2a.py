#!/usr/bin/env python3
ip_addr_inp = input('Input ip address :')
ip_addr = ip_addr_inp.split('.')
for octet in ip_addr:
    if str(octet).isalpha():
        print('Ip address contains letters')
    elif int(octet) < 0 or int(octet) > 255:
        print('Ip address contains out of range octets')

if 1 < int(ip_addr[0]) and int(ip_addr[0]) < 223:
    print("Unicast")
elif 224 < int(ip_addr[0]) and int(ip_addr[0]) < 239:
    print("Multicast")
elif ip_addr_inp == '255.255.255.255':
    print("local broadcast")
elif ip_addr_inp == '0.0.0.0':
    print("Unassigned")
else:
    print("Unused")

