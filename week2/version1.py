import math
# this function is the entry point to the program
def main():
    radiusString = input("Enter the radius of your circle: ")
    radiusInt = int(radiusString)
    printAreaAndPerimeter(radiusInt)

# Takes the radius of a circle as parameter,
# and prints the area and perimeter
def printAreaAndPerimeter(rad):
    circumference = 2 * math.pi * rad
    area = math.pi * rad * rad
    print ("The cirumference of your circle is: ",circumference,\
            ", and the area is: ",area)

if __name__ == '__main__':
    main()

