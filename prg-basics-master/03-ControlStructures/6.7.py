#Child: under 13
#Teen: 13 to 19
#Adult: 20 to 64
#Senior: 65 or olde
age = int(input("Enter your age: "))
if age >= 65:
    print("Senior")
elif age >= 20:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")