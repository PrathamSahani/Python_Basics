# Python Program to Check Perfect Number

n = int(input())
sum =0
for i in range(1, n):
    if n%i==0:
        sum+=i              
    
if(sum==n):
    print("true")
else:
    print("False")