#!/usr/bin/env python3
ip_addr = input('Input ip address (a.b.c.d/mask):')
ip_tmp = ip_addr.split('/')[0]
first, second, third, fourth = ip_tmp.split('.')
mask = ip_addr.split('/')[-1]
print(type(mask))
ip_addr_template = '''
IP address:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
mask_template = '''
Mask:
mask

'''
print(ip_addr_template.format(int(first),int(second),int(third),int(fourth)))
