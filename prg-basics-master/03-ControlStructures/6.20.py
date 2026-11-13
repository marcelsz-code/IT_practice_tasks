#Read a decimal number from the keyboard.
#Divide the number by 2 and note the remainder.
#Divide the quotient obtained by 2 and note the remainder.
#Repeat the same process till we get 0 as the quotient.
#Write the values of all the remainders starting from the bottom to the top. That will be the required binary number.

#decimal_number = int(input('Enter decimal number: '))
#while decimal_number == 0:
    #number = decimal_number / 2
    #remainder = decimal_number % 2
    #print('remainder: ',remainder)
    #number = decimal_number

n = int(input("Enter decimal number: "))
temp = n #iloraz
binary = "" #wynik traktowany jako tekst; zapisanie cyfr obok siebie

while temp > 0:
    binary = str(temp % 2) + binary #dokleja każdą nową resztę na początek
    temp //= 2

print(f"{n}(10) = {binary or '0'}(2)")

