###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = 8
diagonal = math.sqrt(a**2+b**2) # z tw Pitagorasa
diagonal = round(diagonal,2) # zaokrąglenie do 2 miejsc
print(diagonal)