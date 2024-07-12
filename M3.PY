def area_circle (radius):
    return pi*radius**2
def area_rectangle (length,width):
    return length*width
radius=float(input("enter the radius:"))
length=float(input("enter the length:"))
width=float(input("enter the width:"))
pi=3.14
c=area_circle (radius)
r=area_rectangle (length,width)
print("area of circle is:",c)
print("area of rectangle is:",r)