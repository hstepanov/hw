#!/usr/bin/env python3
ip_addr = input('Input ip address (a.b.c.d/mask):')
ip_tmp = ip_addr.split('/')[0]
first, second, third, fourth = ip_tmp.split('.')
mask = ip_addr.split('/')[-1]
ip_addr_template = '''
IP address:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
mask_tmp = []
for bit in range(int(mask)):
    mask_tmp.append(1)
while 32 != int(len(mask_tmp)):
    mask_tmp.append(0)
m_first = int(''.join([str(num) for num in mask_tmp[:8]]), 2)
m_sec = int(''.join([str(num) for num in mask_tmp[8:16]]), 2)
m_third = int(''.join([str(num) for num in mask_tmp[16:24]]), 2)
m_fourth = int(''.join([str(num) for num in mask_tmp[-8:]]), 2)
print(ip_addr_template.format(int(first),int(second),int(third),int(fourth)))
mask_template = '''{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}'''
print('Mask:')
print(mask)
print(mask_template.format(m_first,m_sec,m_third,m_fourth))
