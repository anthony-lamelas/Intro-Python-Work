"""
Author: [Anthony Lamelas]
Assignment / Part: HW3 - Q2 
Date due: February 15, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""

day = str(input("Enter the day the call started at: "))
time = int(input("Enter the time the call started at (hhmm): "))
duration = int(input("Enter the duration of the call (in minutes): "))
total = 0

if day == "Mon" or day == "Tue" or day == "Wed" or day == "Thr":
    if time >= 530 and time<= 2100:
        total = duration*0.55
    else:
        total = duration*0.35
elif day == "Fri" or day == "Sat" or day == "Sun":
    total = duration*0.1
    
print("This call will cost $", round(total,2), sep ="")