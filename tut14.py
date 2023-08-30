# Python Tuples

# tuple = (4, 6 ,8, 10,12,14)
# print(tuple)

# mix = (4,"Python", 9.3)
# print(mix)

# nested = ("Python", {4:5, 6:2, 8:2}, (5, 3,5,3))
# print(nested)

tuple = ("Python", "Tuple", "Ordered", "Colelction")
# print(tuple[0])
# print(tuple[1])

# try:
#     print(tuple[3])
# except Exception as e:
#     print(e)
    
# try:
#     print(tuple[1.0])
# except Exception as e:
#     print(e)
# tuple = ("Tuple", [4, 2,5], (6, 7,8))

# print(tuple[0][3])
# print(tuple[1][1])

# print(tuple[-1])


# tuple = tuple*3
# print(tuple)

# res = tuple.count("Tuple")
# print(res)

# n = (1,2,1,2,3,4,5,6,76,7,442,13,4,324,34,5457)
# res1 = n.count(2)
# print(res1)
# r = n.index(2)
# re = n.index(2, 3)
# print(re)



res = ("Tuple", "Python", "ordered", "Immutable")
for item in res:
    print(item, end=" ")

res1 = ("Ok", "Nice", "GM")
print(res+res1)
print(res1+(4, 5, 6))