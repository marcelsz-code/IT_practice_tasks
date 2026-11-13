from calendar import firstweekday

x = float(input("x = "))
y = float(input("y = "))
quadrant = 0

if x > 0 and y > 0:
    quadrant = 'first quadrant'
elif x < 0 and y > 0:
    quadrant = 'second quadrant'
elif x < 0 and y < 0:
    quadrant = 'third quadrant'
elif x > 0 and y < 0:
    quadrant = 'fourth quadrant'
else:
    quadrant = 'center'
print(f'Point P({x},{y}) is in the {quadrant} of the coordinate system')