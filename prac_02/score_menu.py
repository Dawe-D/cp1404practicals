
""" CP1404 - Prac 2 "Menu" """

MENU = "Menu \n G: Get a valid score (0 - 100 inclusive) \n P: Print Score \n S: Show stars \n Q: Quit"

def main():

    print(MENU)
    choice = input("> ").upper()
    score = None

    while choice != "Q":
        if choice == "G":
            score = get_score()
            print()
        elif choice == "P":
            if score != None:
                result = determine_result(score)
                print(result)
                print()
            else:
                print("No score provided. Please enter Score")
                print()
        elif choice == "S":
            if score != None:
                stars = convert_to_stars(score)
                print(stars)
                print()
            else:
                print("No score provided. Please enter Score")
                print()
        else:
            print("Invalid option.")
        print(MENU)
        choice = input("> ").upper()
    print("Thank you. Goodbye")

def get_score() -> float:
    score = float(input("Enter score: "))
    return score

def determine_result(score: float):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def convert_to_stars(score: float):
        return "*" * int(score)

main()
