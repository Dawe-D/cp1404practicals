"""
CP1404 - Prac 6
Task - Guitars!
Time
Estimate = 40 mins
Actual   = 45 mins
"""

from guitar import Guitar

print("My guitars!")
guitars = []

# --- Quick testing helper: comment these in/out to avoid typing each run ---
# Uncomment the next three lines to prefill for testing instead of typing
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

# Interactive input

while True:
    name = input("Name: ").strip()
    if name == "":
        break

    year = input("Year: ").strip()
    while not (year.isdigit() and int(year) > 0):
        print("Please enter a valid year (integer).")
        year = input("Year: ").strip()

    cost = input("Cost: $").strip()
    try:
        cost = float(cost)
    except ValueError:
        print("Invalid cost; setting to $0.00")
        cost = 0.00

    guitars.append(Guitar(name, int(year), cost))
    print(f"{name} ({year}) : ${cost:,.2f} added.\n")

print("\nThese are my guitars:")

for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
