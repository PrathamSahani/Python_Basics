# Python Program to Check Prime Number

# print("Enter a number :")
# num = int(input())
# p =0
# for i in range(2, num):
#     if num%i==0:
#         p =1
#         break
# if p==0:
#     print( str(num)+ " Prime Number")
# else:
#     print("Not Prime Number ")


def checkPrime(x):
    for i in range(2, x):
        if x%i==0:
            return 1
        
print("Enter a number :")
n = int(input())
chk = checkPrime(n)
if(chk!=1):
    print("Prime")
else:
    print("Not prime")