"""
Author: [Your name here]
Assignment / Part: HW2 - Q1 (etc.)
Date due: February 08, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import random
import math

random = random.randrange(1,20)
root = round(math.sqrt(random),2)
area = round((math.pi)*(root**2),2)


print("Area of a circle with radius", root, "is:", area)