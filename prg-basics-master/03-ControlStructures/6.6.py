
time= int(input('Enter time: '))
if time < 0:
    print("Invalid time")
if time > 6:
    print("Pay 20 PLN")
elif time >= 3:
    print("Pay 15 PLN")
elif time >= 1:
    print("Pay 5 PLN")
else:
    print("Your stop is free of charge")