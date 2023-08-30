# Python Program to Find Sum of First and Last Digit

print("Enter a Number : ")
num = int(input())

count =0
while num!=0:
    if count==0:
        last = num%10
        count = count+1
    rem = num%10
    num = int(num/10)
sum = rem+last
print("Sum : ", sum)