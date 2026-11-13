dog_age = int(input('Enter dog age in human age: '))
dog_agee = 0
if dog_age == 1:
    print("The dog's age in dog's years is 10.5 years")
elif dog_age == 2:
    print("The dog's age in dog's years is 21 years")
elif dog_age > 2:
    dog_agee = (dog_age - 2) * 4+ 21
    print(f"The dog's age in dog's years is {dog_agee} years")