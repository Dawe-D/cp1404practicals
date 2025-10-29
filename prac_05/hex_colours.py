"""
CP1404 - Prac 5
Task - Hex Colour dictionary
"""

NAME_TO_CODE = {"Absolute Zero": "#0048ba", "Barn Red": "#7c0a02", "Battleship Gray": "#848482",
                "British Racing Green": "#004225", "Burnt Orange": "#cc5500", "Byzantine": "#bd33a4",
                "Canary Yellow": "#ffef00", "Desert Sand": "#edc9af", "Ghost White": "#f8f8ff", "Black": "#000000"}

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(f"{colour_name} is {NAME_TO_CODE[colour_name]}")
    except KeyError:
        print("Name not found please enter another")
    colour_name = input("Enter colour name: ").title()
