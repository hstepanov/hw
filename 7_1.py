#!/usr/bin/env python3
with open('ospf.txt', 'r') as fl:
    for ospf_route in fl:
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

