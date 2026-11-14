import sys
import math

radius = float(sys.argv[1])
area = math.pi * radius * radius 
circumference = 2 * math.pi * radius

print("Radius:",radius)
print("Area of circle:",area) 
print("Circumference:",circumference)

