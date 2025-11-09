"""
CP1404 - Prac 7
Task - More Guitars!
"""

from guitar import Guitar

def main():
    guitars = []
    load_guitars(guitars)
    print_guitars(guitars)

def print_guitars(guitars):
    for guitar in sorted(guitars):
        print(guitar)


def load_guitars(guitars):
    in_file = open("guitars.csv", "r")
    for guitar in in_file:
        parts = guitar.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

main()