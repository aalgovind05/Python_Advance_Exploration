
import math

def circle(radius):
    circumfence = 2*math.pi*radius
    area = math.pi *radius**2
    return area, circumfence
a,b = circle(2)
print("area",a," and ","circumfence",b)
