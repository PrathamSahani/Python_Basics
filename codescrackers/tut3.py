# Python Program to Check Armstrong or Not


n =int(input())
temp = n
rev =0
while temp!=0:
    res= temp%10
    rev += res**len(str(n))
    temp = temp//10
    
if rev==n:
    print("Its Armstrong")
else:
    print("Its Not Armstrong")