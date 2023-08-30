# Python Program to Add Digits of a Number


# print("Enter a Number : ")
# n = int(input())
# sum =0
# while n>0:
#     res = n%10
#     sum = res+sum
#     n = int(n/10)
# print("Sum of Digits of Given number : ", sum)



# print(end = "Enter a Number :")
# num = int(input())
# sum =0
# print(end="\n")
# while num>0:
#     rem = num%10
#     sum = sum+rem
#     num = int(num/10)
    
#     if(num==0):
#         print(end=str(rem))
#     else:
#         print(end=str(rem)+"+")
# print(" = "+str(sum))



def addNumDig(n):
    sum =0
    while n>0:
        rem = n%10
        sum = rem+sum
        n = n//10
    return sum
print("Enter a Number : ", end="")
num = int(input())
res = addNumDig(num)
print("Sum of Digit  is : "+str(num)+" = "+str(res))