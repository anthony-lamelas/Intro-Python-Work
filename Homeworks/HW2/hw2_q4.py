"""
Author: [Your name here]
Assignment / Part: HW2 - Q1 (etc.)
Date due: February 08, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct
"""

ting_days = int(input("Enter the number of days Ting has worked:"))
ting_hours = int(input("Enter the number of hours Ting has worked:"))
ting_minutes = int(input("Enter the number of minutes Ting has worked:"))

justin_days = int(input("Enter the number of days Justin has worked:"))
justin_hours = int(input("Enter the number of hours Justin has worked:"))
justin_minutes = int(input("Enter the number of minutes Justin has worked: "))


tdays = ting_days + justin_days
thours = ting_hours + justin_hours
tminutes = ting_minutes + justin_minutes



print("The total time both CAs worked together is:", tdays, "days,", thours, "hours, and", tminutes, "minutes")