# Python Program to Check Palindrome Number


print("Enter a  number ")
n = int(input())
rev =0
temp = n
while temp>0:
    rem = temp%10
    rev =rem+(rev*10)
    temp = temp//10
if rev==n:
    print("Yes")
else:
    print("No")