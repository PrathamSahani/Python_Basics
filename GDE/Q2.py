# Get user input for age
age = int(input("Enter your age: "))

# Check age to determine eligibility
if age >= 18:
    # Nested if-else statement
    if age >= 65:
        print("You are eligible for senior citizen benefits.")
    else:
        print("You are eligible to vote.")
else:
    print("You are not eligible for voting.")

# This message is always printed, regardless of age
print("Thank you for checking your eligibility.")
