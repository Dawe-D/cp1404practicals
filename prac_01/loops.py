for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Question A

for a in range(0, 100, 10):
    print(a, end=' ')
print()

# Question B

for b in range(20, 0, -1):
    print(b, end=' ')
print()

# Question C

number_of_stars = int(input("Number of stars: "))

for c in range(number_of_stars):
    print("*", end='')
print()

# Question D

for d in range(number_of_stars + 1):
    for n in range(d):
        print("*", end='')
    print()
