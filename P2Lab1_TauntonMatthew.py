#Matthew E. Taunton
#11/14/2024
#P2LAB1
# program will calculate the diameter, circumference, and area of a circle.

import math

radius = float(input('what is the radius of the circle? '))

diameter = radius * 2
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print('\nThe diameter of a circle is ',diameter)
print('\nThe circumference of a circle is ',circumference)
print('\nThe area of a circle is ',area)
