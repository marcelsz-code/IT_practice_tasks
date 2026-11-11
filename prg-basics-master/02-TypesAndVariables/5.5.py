#The price of the product on the price tag is given before and after the discount is applied. Write a program that allows you to enter the product price and discount. Print the product price, discount, discounted product price, and the difference between the product price before and after the discount. Print all prices with two decimal places.
# Sample result:
# Enter price: 24.72
# Enter discount %: 15
# Price with discount: 21.01
# Reduction: 3.71

first_price = float(input('Enter price: '))
discount = float(input('Enter discount %: '))
price_with_discount = first_price - (discount/100 * first_price)
reduction = first_price * (discount/100)
print(f'Enter price: {first_price:.2f}, Enter discount: {discount}, Price with discount: {price_with_discount:.2f} Reduction: {reduction:.2f}')