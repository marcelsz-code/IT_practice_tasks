#23% VAT was paid from an amount. Write a program that reads an amount from the keyboard.
# Then, it calculates and prints both the amount and its VAT. Apply formatting with two decimal places. Sample result:
#Amount  : 15.84
#VAT 23% :  3.64

amount = float(input('Amount: '))
Vat = amount * 0.23
total = Vat + amount

print(f'amount = {amount:.2f}, Vat 23% = {Vat:.2f}, total = {total:.2f}')