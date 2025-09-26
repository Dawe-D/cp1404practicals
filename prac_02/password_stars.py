PASSWORD_LENGTH_MIN = 8

def main():

    user_password = get_password()
    print()

    convert_to_stars(user_password)


def convert_to_stars(user_password: str):
    for n in user_password:
        print("*", end='')
    print()


def get_password() -> str:
    user_password = input("Please enter a password: ")

    while len(user_password) < PASSWORD_LENGTH_MIN:
        print("Password not long enough. Please enter a minimum of 8 characters.")
        user_password = input("Please enter a password: ")
    return user_password


main()
