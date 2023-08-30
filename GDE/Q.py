# Subproblem 1: Calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Subproblem 2: Get user input for the number
def get_user_input():
    try:
        num = int(input("Enter a number: "))
        return num
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_input()

# Main function
def main():
    num = get_user_input()
    result = factorial(num)
    print(f"The factorial of {num} is {result}")

if __name__ == "__main__":
    main()
