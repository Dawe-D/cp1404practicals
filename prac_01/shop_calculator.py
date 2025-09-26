
number_of_items = int(input("Enter the number of items: "))
total_price = 0

while number_of_items < 0:
    print("Invalid Number of items!")
    number_of_items = int(input("Enter the number of items: "))

for i in range(number_of_items):
    price = float(input(f"Enter price of item {i + 1}: "))
    total_price += price

if total_price > 100:
    total_price *= 0.9

print(f"Total price: ${total_price:.2f}")
