"""
Prac 3
Task - Files
"""

# 1
FILE_NAME = "name.txt"

out_file = open(FILE_NAME, 'w')

user_name = input("Please enter your name: ")
print(user_name, file=out_file)

out_file.close()

# 2
file_name = open("name.txt", 'r')
name = file_name.read().strip()

print(f"Hi {name}!")
print()

file_name.close()

# 3

with open("numbers.txt", 'r') as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
    result = first_number + second_number
print(result)
print()

#4
total_of_all_lines = 0

with open("numbers.txt", 'r') as file:
    for line in file:
        number = int(line)
        total_of_all_lines += number
    print(total_of_all_lines)
