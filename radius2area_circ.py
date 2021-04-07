import math #import math library to have access to value of pi
def circlefunc(radius):
	circumf=(2*math.pi*radius)#calculate circumference (2(pi)r)
	area= math.pi*(radius**2)#calculate area of circle ((pi)r^2)
	print("circumference:", circumf, "area:",area)
	return circumf,area

circlefunc(int(input("Enter Radius: ")))
