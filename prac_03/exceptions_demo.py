"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When someone enters a floating/decimal number or string.
2. When will a ZeroDivisionError occur?
    When the user inputs zero as the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    It would rely on the user reading the input notation. This is not foolproof.
    Or use a while loop to check denominator = 0 and re request input if true.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
