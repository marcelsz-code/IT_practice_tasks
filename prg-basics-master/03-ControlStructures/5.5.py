###
# Sums numbers entered by user
#
from gettext import c2py
from itertools import count

total_sum = 0
c = 0
while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    c += 1

print(f"The total sum of the numbers is: {total_sum}")
if c > 0:
    arithmetic = total_sum / c
    print(f'The arithmetic mean is: {arithmetic}')
else:
    print('The arithmetic mean is 0')