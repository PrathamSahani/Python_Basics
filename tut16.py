# add = lambda num: num+4
# print(add(6))

# a = lambda x, y:(x*y)
# print(a(4,5))

# b = lambda x, y, z :(x+y+z)
# print(b(4, 5, 5))

# list_ = [35, 12, 69, 55, 75]
# odd_list = list(filter(lambda num:(num%2!=0), list_))
# print(odd_list)


# lis  = [2,4, 5, 6, 7,9,10]
# sqre = list(map(lambda num: num**2, lis))
# print(sqre)


# squre = [lambda num= num:num**2 
#         for num in range(0, 11)]
# for square in squre:
#     print(square(), end=" ")
    
    
# Mini = lambda x, y:x if(x<y)else y 
# print(Mini(35, 74))



list = [[3, 5, 8, 6], [23, 54, 12, 87], [1, 2,4,12, 5]]
sort = lambda num:(sorted(n) for n in num)

third = lambda num, func:[l[len(l)-2]for l in func(num)]

res = third(list, sort)
print(res)