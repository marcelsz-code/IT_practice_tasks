number = 2
print(f"Enter a number of products purchased:{number}")
price = 40
print(f"Product price: {price}")
if number > 2:
    number = number - 2
    new_price = number * (0.75 * price)
    new_price = new_price + 2 * price
    print(f"amount to pay: {new_price}")

elif number == 2:
    new_price = price * 2
    print(f"Amount to pay: {new_price}")
else:
    print("Amount to pay: 40.00")

