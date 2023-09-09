#Data types: Numbers
#modulo can be used to determine odd and even numbers
#round(num, decimalPlaces)
#import math (brings in math module of functions)
#math.factorial(5) 5*4*3*2*1 math.floor rounds up math.floor rounds


#Calculate the area and circumference of a circle. Ask the user for the radius.

#my attempt
#import math

#radius = input("Give me the radius and I'll calculate the area and circumference of a circle!")
#area = math.pi(radius **2)

#circumference = 2 * (math.pi(radius))

#print("Area:", area)
#print("Circumference:", circumference)

#questions: difference between using "," and "+"; 

# multi line comment with """

import math

print("This program will calculate the area and circumference of a circle given its radius")
radius = float(input("Type the radius of the circle: "))
area = math.pi * (radius **2) #parentheses for heirarchy of operations
circumference = 2 * math.pi * radius

print("The area of the circle is", round(area, 2), "The circumference is:", round(circumference, 2))

#I want to commit this file to github
#Steps: ???

