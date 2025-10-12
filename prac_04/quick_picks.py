"""
CP1404 Prac 4
Lottery Ticket Generator
"""

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_IN_PICK = 6

import random

number_of_picks = int(input("How many quick picks? "))

for n in range(number_of_picks):
    numbers = []
    while len(numbers) < NUMBERS_IN_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    print(" ".join(f"{number: >2}" for number in numbers))
