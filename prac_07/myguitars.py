"""
CP1404 - Prac 7
Task - More Guitars!
"""

from guitar import Guitar

def main():
    guitars = []
    in_file = open("guitars.csv", "r")
    for guitar in in_file:
        parts = guitar.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    guitars.sort()
    for guitar in guitars:
        print(guitar)

main()