#!/usr/bin/env python3
# script waits for ip address input. if it's incorrect, script promt is again
while True:
    try:
        ip_addr = input('Input ip address :').split('.')
        if len(ip_addr) != 4:
            ip_addr = input('Input ip address :').split('.')
        for octet in ip_addr:
            if octet.isalpha():
                break
            elif int(octet) < 0 or int(octet) > 255 or octet == '':
                break
            elif not octet.isdigit():
                break
    except:
        print('Input valid ip address')
    else:
        break
try:
    if 1 <= int(ip_addr[0]) and int(ip_addr[0]) <= 223:
        print("Unicast")
    elif 224 <= int(ip_addr[0]) and int(ip_addr[0]) <= 239:
        print("Multicast")
    elif ip_addr == '255.255.255.255':
        print("local broadcast")
    elif ip_addr == '0.0.0.0':
        print("Unassigned")
    else:
        print("Unused")
except:
    print('Script execution aborted. Shit happens')
