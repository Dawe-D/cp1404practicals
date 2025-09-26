"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter Sales: $"))

while sales >= 0:
    if sales < 1000:
        sales_10 = sales * (10 / 100)
        print(f"Result: ${sales_10: .2f}")
    else:
        sales_15 = sales * (15 / 100)
        print(f"Result: ${sales_15: .2f}")
    sales = float(input("Enter Sales: $"))