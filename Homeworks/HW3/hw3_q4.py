"""
Author: [Anthony Lamelas]
Assignment / Part: HW3 - Q4
Date due: February 15, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""
import math

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

solution1 = 0
solution2 = 0

discrim = (b**2) - (4*a*c)

#infinite if all 0
#no solution if a is 0
# no real solution if discrim is negative

if a == 0 and b !=0 and c!=0:
    solution1 = b/(-1*c)
    print("This equation has one solution: x = " , solution1)
    
elif a == 0 and b == 0 and c != 0:
    print("This equation has no solution.")
    
elif a == 0 and b == 0 and c == 0:
    print("This equation has infinite solutions")
    
elif discrim < 0:
    print("This equation has no real solution")
    
elif discrim == 0:
    solution1 = ((-1*b) + (math.sqrt((b**2)-4*a*c)))/(2*a)
    print("This equation has one solution: x = " , solution1)
    
elif discrim > 0:
    solution1 = ((-1*b) + (math.sqrt((b**2)-4*a*c)))/(2*a)
    solution2 = ((-1*b) - (math.sqrt((b**2)-4*a*c)))/(2*a)
    print("This equation has two solutions: x = " , solution1, "and x = ", solution2)
    
    
    





