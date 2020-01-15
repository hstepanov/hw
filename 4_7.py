mac = 'AAAA:BBBB:CCCC'
doc = mac.replace(':','')
integer = int(doc, 16)
print(f"{int(integer):48b}")
#print(format(integer, '0>48b'))
