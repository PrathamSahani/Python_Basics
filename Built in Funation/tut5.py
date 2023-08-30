# Python bin() Function

# print("Enter Any Number : ", end="")
# num = int(input())
# print(bin(num))

x = int(input())
try:
    xbin = bin(x)
    print("\nBinary Equivalent of ", x, "is", xbin)
except TypeError:
    print("Invalid Argument ")