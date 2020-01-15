vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
vlans.sort()
vlans_set = set(vlans)
vlans_uniq = list(vlans_set)
vlans_uniq.sort()
print(vlans_uniq)
