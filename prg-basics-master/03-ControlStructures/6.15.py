barcode = input('Enter EAN-13 article number: ')
if barcode.isdigit() and len(barcode) == 13:
    print('article number is correct')
if barcode[:3] == '590':
    print('Article manufactured in Poland')