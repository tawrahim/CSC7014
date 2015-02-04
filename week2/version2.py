import math

# entry point to the program.  
def main():
        radius = int( input("Enter the radius of your circle: ") )
        area, perimeter = computeAreaAndPerimeter(radius)
        print ("The cirumference of your circle is: ",perimeter,\
                "\nThe area of your circle is: ",area)
    

# takes the radius of a circle as paramter and
# returns its area and circumference
def computeAreaAndPerimeter(rad):
    circumference = 2 * math.pi * rad
    area = math.pi * rad * rad
    return area, circumference

if __name__ == '__main__':
    main()
