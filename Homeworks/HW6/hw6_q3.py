"""
Author: [Anthony Lamelas]
Assignment / Part: HW6 - Q3
Date due: March 07, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""

letters = str(input("Enter a string of lowercase letter: "))
count = 1
index = 0


while index < len(letters)-1 and count == 1:
    if letters[index] <= letters[index+1]:
        print(letters, "is not decreasing")
        print("It stopped being lexicographically decreasing at location", index+1)
        count += 1
    index+=1
    
    
        
        
        
if count == 1:
    print(letters, "is decreasing.")