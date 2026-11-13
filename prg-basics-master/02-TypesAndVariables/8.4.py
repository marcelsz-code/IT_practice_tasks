###
# A program that prints your height both in cm and in feet and inches.
#
cm = 186
inches = round (cm/2.54)
feet= inches //12
remainder = inches % 12 # calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {remainder} inches')