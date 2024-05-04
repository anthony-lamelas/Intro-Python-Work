"""
Author: [Anthony Lamelas]
Assignment / Part: HW5 - Q2 
Date due: February 29, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""


GRAVITY = 9.81

velocity = (input("Enter the initial velocity (m/s) or type 'DONE' to quit: "))

    


while velocity != "DONE":
    
    while float(velocity) < 1:
        velocity = (input("velocity must be greater than 0. Enter a valid velocity: "))

        
    max_height = (float(velocity) **2)/ (2*GRAVITY)
    time = float(velocity)/GRAVITY
    
    print("For initial velocity =", velocity, "m/s: ")
    print("Max height reached: ",round(max_height,2), "meters")
    print("Time to reach max height:", round(time,2), "seconds")


    velocity = (input("Enter the initial velocity (m/s) or type 'DONE' to quit: "))
    

print("Program ended")
    

