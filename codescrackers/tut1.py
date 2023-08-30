# Python Program to Check Even or Odd Number


# num = int(input())
# if num%2==0:
#     print("True")
# else:
#     print("false")


def check(n):
    if n%2==0:
        return 1
print("Enter a Number ", end="")
num = int(input())

chk = check(num)
if chk==1:
    print("Yup")
else:
    print("Nope")