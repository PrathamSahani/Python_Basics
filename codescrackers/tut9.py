# Add Digits of a Number using while Loop

# print('Enter a number ')
# num = int(input())
# rem =0
# while num>0:
#     dig = num%10
#     rem = rem+dig
#     num = num//10
    
# print(rem)

def addNumDig(n):
    sum =0
    while n>0:
        rem = n%10
        sum = sum+rem
        n = int(n/10)
    return sum
print("Enter a Number : ")
num = int(input())
res = addNumDig(num)
print(str(num)+" = "+str(res))
