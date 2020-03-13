#!/usr/bin/env python3
ip_inp = input('Input ip address :').split('.')
ip_addr = []
for octet in ip_inp:
    if octet.isalpha(): 
        print('Ip address is incorrect')
        break
    elif int(octet) < 0 or int(octet) > 255: 
        print('Ip address is out of range')
        break
    else:
        ip_addr.append(octet)
if len(ip_addr) == 4:
    try:
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
    except:
        print('Script execution aborted')
