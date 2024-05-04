"""
Author: [Anthony Lamelas]
Assignment / Part: HW4 - Q5 
Date due: February 22, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct
"""

n = int(input("Please enter a positive integer: "))

layer = (2*n) - 1
original = (2*n) - 1
temp = ""
temp1 = 3
temp2 = ""

while layer > 0:
    space = (original - layer) //2
    temp =  layer *("*")
    layer -=2
    print(" " * space + temp)


while temp1 < original +1:
    space = (original - temp1) //2
    temp2 = temp1*("*") 
    temp1 += 2
    print(" " * space + temp2)