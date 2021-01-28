import math
#calcpkg/operation.py 
def squareroot(n):
    return math.sqrt(n)
    
#calcpkg/geometry.py
def circle_area(radius):
    return radius * radius * math.pi

from calcpkg.operation import squareroot as root
from calcpkg.geometry import circle_area as area
 
num = int(input())
print(root(num))
print(area(num))

