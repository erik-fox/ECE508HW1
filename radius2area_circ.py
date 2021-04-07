import math
def circlefunc(radius):
	circumf=(2*math.pi*radius)
	area= math.pi*(radius**2)
	print("circumference:", circumf)
	print("area:",area)
	return circumf,area

circlefunc(int(input("Enter Radius: ")))
