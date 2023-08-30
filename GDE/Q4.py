# Function to calculate the sum of cubes of individual digits
def cubesum(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** 3
        num //= 10
    return total

# Function to check if a number is an Armstrong number
def isArmstrong(num):
    return num == cubesum(num)

# Function to print Armstrong numbers within a given range
def PrintArmstrong(start, end):
    for num in range(start, end + 1):
        if isArmstrong(num):
            print(num)

# Main program
if __name__ == "__main__":
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        
        if start < 0 or end < 0:
            print("Please enter non-negative integers for the range.")
        else:
            print(f"Armstrong numbers between {start} and {end}:")
            PrintArmstrong(start, end)
    
    except ValueError:
        print("Invalid input. Please enter valid integers for the range.")
