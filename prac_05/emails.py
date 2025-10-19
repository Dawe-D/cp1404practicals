"""
CP1404 - Prac 5
Task - Emails
Estimate -  35 mins
Actual   - 33 mins
"""


def main():
    email_to_name = {}
    email = input("Please enter Email: ")

    while email != "":
        possible_name = extract_name(email)
        confirm_name = input(f"Is your name {possible_name}? \n Y/N: ").upper()

        while confirm_name not in ["", "Y", "N"]:
            print("Invalid Input. Please enter Y or N.")
            confirm_name = input(f"Is your name {possible_name}? \n Y/N: ").upper()

        if confirm_name == "" or confirm_name == "Y":
            email_to_name[email] = possible_name
        else:
            name = input("Enter Name: ")
            email_to_name[email] = name

        email = input("Please enter Email: ")

    longest_name = max(len(name) for name in email_to_name.values())

    for email, name in email_to_name.items():
        print(f"{name:{longest_name}} : {email}")


def extract_name(email):
    possible_name = email.split("@")[0]
    if "." in possible_name:
        possible_name_parts = possible_name.split(".")
        name = " ".join(possible_name_parts).title()
    else:
        name = possible_name.title()
    return name


main()
