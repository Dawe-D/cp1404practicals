"""
CP1404 - Prac 3
Task - Randoms

"""

import random

# A random number between 5 and 20. Lowest could have been 5 and highest could have been 20

# A random odd number between 3 and 10. Lowest was 3 and highest was 9. This code cannot produce an even number as the range starts at 3 and has a step of 2.

# A random number with a large number of decimals. Assumed lowest is 2.5 and assumed largest would be 5.5.

random_number = random.randint(0,100)
print(random_number)
