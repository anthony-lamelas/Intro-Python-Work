"""
Author: [Anthony Lamelas]
Assignment / Part: HW6 - Q4 
Date due: March 07, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""

code = str(input("Enter an encoded string: "))
key = int(input("Enter a key: "))


message = ""


index = len(code)-1
step = key+1
while index >= 0:
    
    if not code[index].isdigit():
        message += code[index]
        
    index -= step
 
    
    
print(message)

