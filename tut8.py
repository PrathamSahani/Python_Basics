# merge two list  , dict1

l1 = [10, 20, 30, 40]
l2 = [50, 60, 10]

dict1={"a": 10, "b": 20}
dict2 = {"c": 30, "d":40}

# merged_list = l1+l2
# print(merged_list)
# merged_list.sort()
# merged_list.reverse()
# print(merged_list)


# dict.update(dict2)
# print(dict)


# merged1 = {**dict1, **dict2}
# print(merged1)

# l1.extend(l2)
# print(l1)

from itertools import chain
merged1 = list(chain(l1, l2))
print(merged1)

mer = dict(dict1, **dict2)
print(mer)