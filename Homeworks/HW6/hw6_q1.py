"""
Author: [Anthony Lamelas]
Assignment / Part: HW6 - Q1 
Date due: March 07, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""

initials = str(input("Enter the initials of the suspects: "))
wrapper = str(input("Enter the candy wrappers: "))
count = 0


for index in initials:
    if index in wrapper:
        print(index, "is a candy thief suspect")
        count += 1
        
if count == 0:
    print("No candy thief found")
    