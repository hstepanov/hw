#!/usr/bin/env python3
ip_addr = input('Input ip address :')
try:
    first_octet = int(ip_addr.split('.')[0])
    second_octet = int(ip_addr.split('.')[1])
    third_octet = int(ip_addr.split('.')[2])
    fourth_octet = int(ip_addr.split('.')[3])
    octets_list = [first_octet, second_octet, third_octet, fourth_octet]
    for octet in octets_list:
        if not str(octet).isdigit():
            print('Ip address is not correct')

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
except ValueError:
    print('you input letters')

#for octet in octets_list:
#    if not str(octet).isdigit():
#        print('Ip address is not correct')

#for octet in octets_list:
#        if octet <= 0 or octet > 255:
#            print('Ip address is not correct')
#            break

