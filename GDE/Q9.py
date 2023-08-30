# def sort(arr):
#     if(arr[i]<=arr[i+1] for i in range(len(arr)-1)):
#         return "Asce"
#     if(arr[i]>=arr[i+1] for i in range(len(arr)-1)):
#         return "Desc"
    
#     return "equal"

# items = input("Enter ").split()

# items = [int(item) for item in items]

# ans = sort(items)

# if ans=="Asce":
#     print("right")
# elif ans=="Desc":
#     print("Right")
# else :
#     print("Close")



# def square(x):
#     return x**2
# print(square(5))


# res = lambda x: x**2
# res1 = res(4)
# print(res1)


# num = [1, 2,3,4]
# square = list(map(lambda x: x**2, num))
# print(square)



# num = [1,2,3,4,5]
# sqare = [x**2 for x in num]
# print(sqare)

num1 = 1
num2 = 5
res = format(num1+num2, ".2f")
print(res)

# Method 4: Using the math.fsum() function (for high precision)
import math

decimal1 = 3.14
decimal2 = 2.25
result = math.fsum([decimal1, decimal2])
print("Method 4 Result:", result)




