# File: FunctionExamples.py
# Student: Sanjitha Venkata
# UT EID: sv28325
# Course Name: CS303E
# 
# Date Created: 9/22/2023
# Description of Program: Coded multiple functions that perform different math calculations for the most part. 

import math

#----------------------------------------------------------------------
# 1. Returns the sum of three numbers.

def sum3Numbers (x, y, z):
    """Return the sum of the three parameters."""
    return x + y + z

#----------------------------------------------------------------------
# 2. Returns the product of three numbers.

def multiply3Numbers( x, y, z ):
    return x*y*z

#----------------------------------------------------------------------
# 3. Returns the sum of up to 3 numbers. Accepts 1, 2, or 3 parameters.
#    If provided less than 3, that parameter will default to 0. 

def sumUpTo3Numbers (x, y = 0, z = 0):
    return x+y+z

#----------------------------------------------------------------------
# 4. Returns the product of up to 3 numbers. Accepts 1, 2, or 3 parameters.
#    If provided less than 3, that parameter will default to 1.

def multiplyUpTo3Numbers (x, y=1, z=1):  # supply default args
    return x*y*z

#----------------------------------------------------------------------
# 5. Takes 2 numbers as input and prints them out in ascending order.

def printInOrder( x, y ):
    if(x<y):
        print(x,y)
    else:
        print(y,x)

#----------------------------------------------------------------------
# 6. Returns the area of a square, given the length of a side.
#    Does not accept negative parameters.

def areaOfSquare( side ):
    if(side<0):
        print("Negative value entered")
    else:
        return(side*side)

#----------------------------------------------------------------------
# 7. Returns the perimeter of a square, given the length of a side.
#    Does not accept negative parameters.

def perimeterOfSquare( side ):
    if(side<0):
        print("Negative value entered")
    else:
        return(side*4)

#----------------------------------------------------------------------
# 8. Returns the area of a circle, given the radius
#    Does not accept negative parameters.

def areaOfCircle( radius ):
    if(radius<0):
        print("Negative value entered")
    else:
        return(radius*radius*math.pi)


#----------------------------------------------------------------------
# 9. Returns the circumference of a circle, given the radius
#    Does not accept negative parameters.

def circumferenceOfCircle( radius ):
    if(radius<0):
        print("Negative value entered")
    else:
        return(2*math.pi*radius)

#----------------------------------------------------------------------
# 10. Determines if x is evenly divided by d1 and d2.

def bothFactors( d1, d2, x ):
    if(x%d1==0 and x%d2==0):
        return True
    else:
        return False

#----------------------------------------------------------------------
# 11. Given a number computes the area and circumference of a circle
#     and the area and perimeter of a square

def squareAndCircle( x ):
    print("\nCircle with radius",x,"has:")
    print("   Area:", areaOfCircle(x))
    print("   Circumference:",circumferenceOfCircle(x))
    print("Square with side",x,"has:")
    print("   Area:",areaOfSquare(x))
    print("   Perimeter:",perimeterOfSquare(x))
    print()

#----------------------------------------------------------------------
# 12. Returns the factorial of the given integer
#    Does not accept negative parameters.

def factorial( n ):
    fac=1
    if(n<0):
        print("Input must be positive.")
    else:
        for i in range (1,n+1):
            fac *= i
        return fac
        

#----------------------------------------------------------------------
# 13. Returns the number of digits in the given integer

def numberLength( n ):
    count=0
    while(n):
        n=n//10
        count+=1
    return count
#----------------------------------------------------------------------
