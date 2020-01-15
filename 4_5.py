command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
command1_lst = command1.split()
command1_str = str(command1_lst[-1])
command1_lst = command1_str.split(',') 
command2_lst = command2.split()
command2_str = str(command2_lst[-1])
command2_lst = command2_str.split(',')
command1_set = set(command1_lst)
command2_set = set(command2_lst)
result_set = list(command1_set.intersection(command2_set))
print(result_set)
