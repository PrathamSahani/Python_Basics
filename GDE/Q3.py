# import math

# max =50
# print("Print numbers  :")
# for num in range(2, max+1):
#     res = True
#     for i in range(2, int(math.sqrt(num))+1):
#         if num%i==0:
#             res = False
#             break       
#     if res:
#         print(num, end=" ")




import math
def is_print(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    
    for i in range(3, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

print("Alternate Prime numbers from 1 to 50: ")
for num in range(1, 51):
    if is_print(num):
        print(num, end=" ")
        
x =5
print(x*x)