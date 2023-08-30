# How to reverse a number in Python

num = int(input())
rev =0
temp = num
while temp>0:
    res = temp%10
    rev = (rev*10)+res
    temp//=10
    
if(rev==num):
    print("True")
else:
    print("false")