# # Create an empty dictionary to store student data
# student_data = {}

# # Input data for 10 students
# for i in range(1, 4):
#     roll_no = input(f"Enter roll number for student {i}: ")
#     name = input(f"Enter name for student {i}: ")
    
#     # Store the data in the dictionary with roll number as the key
#     student_data[roll_no] = name

# # Print the student data
# print("\nStudent Data:")
# for roll_no, name in student_data.items():
#     print(f"Roll No: {roll_no}, Name: {name}")


set1 = {1, 2, 3,4}
set2 = {1,3, 6, 7}
ans = set2.difference(set1)
print(ans)