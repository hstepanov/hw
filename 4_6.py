ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
protocol = 'OSPF'
prefix = str(ospf_route[9:21])
ad = str(ospf_route[23:29])
nh = str(ospf_route[35:44])
update = str(ospf_route[46:51])
int_out = str(ospf_route[53:70])
print(f"Protocol:           {protocol}")
print(f"Prefix:             {prefix}")
print(f"AD/Metric:          {ad}")
print(f"Next-Hop:           {nh}")
print(f"Last Update:        {update}")
print(f"Outbound Interface: {int_out}")
