config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
config_lst = config.split()
vlan = str(config_lst[-1])
vlan_lst = vlan.split(',')
print(vlan_lst)
