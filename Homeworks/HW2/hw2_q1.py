"""
Author: [Anthony Lamelas]
Assignment / Part: HW2 - Q1 (etc.)
Date due: February 08, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
import math


guests = int(input("Enter the number of guests: "))
slices = int(input("Enter the number of slices each guest will eat: "))

total_slices = guests*slices
min_pizzas = math.ceil((total_slices)/8)
leftovers = (min_pizzas*8) - total_slices

print("Minimum number of whole large pizzas required:", min_pizzas)
print("Total number of large pizza slices needed:", total_slices)
print("Number of large pizza slices left over:", leftovers)

