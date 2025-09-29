"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    score = get_score()
    result = determine_result(score)
    print(result)

    random_score = random.randint(0, 100)
    random_result = determine_result(random_score)
    print(random_score)
    print(random_result)

def determine_result(score: float):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_score() -> float:
    score = float(input("Enter score: "))
    return score


main()
