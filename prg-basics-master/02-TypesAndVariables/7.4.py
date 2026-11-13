#Enter tree circumference in cm: 120
#Tree can be cut down: False
#A tree may be cut down if its diameter is at least 50 cm. Write a program that, based on the circumference of the tree entered from the keyboard,
# calculates and prints the value True if the tree can be cut down, or print the value False otherwise
circumference = int(input('Enter tree circumference in cm: '))
Tree = circumference >= 50
print(f'Tree can be cut down: {Tree}')