supplies = 10.00
shipping = 7.50
discount = 30
tax = 5

total = (supplies-((discount*supplies)/100))+(tax*(supplies-((discount*supplies)/100))/100)+shipping

print(f"Total: {total}")
print("The total includes any applied discounts, sales tax, and shipping cost.\n")


funds = 3.00

if funds > 0:
    print("You have money")
elif funds == 0:
    print("You're out")
else:
    print("You seem to be in debt")