"""
CP1404 Prac 4
Basic list operations
"""

# Part 1
numbers = []

for i in range(5):
    number = float(input("Number: "))
    numbers.append(number)

print()
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of all numbers is {sum(numbers) / len(numbers): .1f}")

# Part 2

valid_usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Please enter username: ")

if username in valid_usernames:
    print("Access granted")
else:
    print("Access Denied")