import math

radiusString = input("Enter the radius of your circle: ")
radiusInt = int(radiusString)
circumference = 2 * math.pi * radiusInt
area = math.pi * radiusInt * radiusInt
print ("The cirumference of your circle is: ",circumference,\
                ", and the area is: ",area)

