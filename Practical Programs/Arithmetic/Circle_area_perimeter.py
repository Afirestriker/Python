
#Accept radius of circle from user, and find area and perimeter
#pie = 3.14
#area = pie*r*r
#perimeter = 2*pie*r

rad = int(input("Enter Radius: "))

print("Given Radius: ", rad)

area = 3.14 * rad * rad
perimeter = 2 * 3.14 * rad

print("Area of circle: ", area)
print("Perimeter of circle: ", perimeter)

print("Data type of Area: ", type(area))
print("Data type of perimeter: ", type(perimeter))
