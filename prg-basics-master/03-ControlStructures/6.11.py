current_price = 1000
print("Current_price:", current_price)
previous_price = 3000
print("Previous_price:", previous_price)
alert = (previous_price - current_price)/previous_price
if alert >= 0.1:
    print('Buy the product!!')
    percent = alert * 100
    print(f'Product price reduced by {percent}%')
else:
    print("It's not worthy")