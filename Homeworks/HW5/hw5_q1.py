"""
Author: [Anthony Lamelas]
Assignment / Part: HW5 - Q1 
Date due: February 29, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""

velocity = (input("Enter the initial velocity (m/s) or type 'DONE' to quit: "))

    


while velocity != "DONE":
    acceleration = float(input("Enter the acceleration (m/s^2): "))
    while acceleration < 1:
        print("Acceleration must be greater than 0.")
        acceleration = float(input("Enter a valid acceleration (m/s^2): "))
            
            
    distance = (float(velocity)**2)/(2*acceleration)
    print("Distance traveled until stop:",round(distance,1),"meters")


    
    
    
    
    velocity = (input("Enter the initial velocity (m/s) or type 'DONE' to quit: "))
    

