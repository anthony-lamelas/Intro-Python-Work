"""
Author: [Anthony Lamelas]
Assignment / Part: HW6 - Q2 
Date due: March 07, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""

max_num = int(input("Enter a positive integer 'max_num': "))

temp = "A"


print("Iteration 1:",temp)

if max_num > 1:
    for i in range (2,max_num+1):
        temp1 = ""
        
        for index in temp:
            if index == "A":
                temp1 += "B"
            
            elif index == "B":
                temp1 += "A"
            
        temp = temp + temp1
        
        print("Iteration ", i, ": ",temp,sep="")
    

        
    
    

    