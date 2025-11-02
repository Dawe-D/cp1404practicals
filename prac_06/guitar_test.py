"""
CP1404 - Prac 6
Task - Guitars!
Time
Estimate = 40 mins
Actual   = 45 mins
"""

from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2013, 2000)

expected_gibson_age = 2022 - 1922
expected_another_age = 2022 - 2013

print(f"{gibson.name} get_age() - Expected {expected_gibson_age}. Got {gibson.get_age()}")
print(f"{another.name} get_age() - Expected {expected_another_age}. Got {another.get_age()}")

print(f"{gibson.name} is_vintage() - Expected {expected_gibson_age >= 50}. Got {gibson.is_vintage()}")
print(f"{another.name} is_vintage() - Expected {expected_another_age >= 50}. Got {another.is_vintage()}")

