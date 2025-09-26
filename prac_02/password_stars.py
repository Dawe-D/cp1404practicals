PASSWORD_LENGTH_MIN = 8

user_password = input("Please enter a password: ")

while len(user_password) < PASSWORD_LENGTH_MIN:
    print("Password not long enough. Please enter a minimum of 8 characters.")
    user_password = input("Please enter a password: ")
print()

for n in user_password:
    print("*", end='')
print()
