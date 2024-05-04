"""
Author: [Anthony Lamelas]
Assignment / Part: HW3 - Q1 
Date due: February 15, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""




print("Welcome to the Lemonade Stand Profit Calculator!")
season = str(input("Enter the current season (summer/other):"))
small = int(input("Enter the number of small cups of lemoneade sold:"))
medium = int(input("Enter the number of medium cups of lemoneade sold:"))
large = int(input("Enter the number of large cups of lemoneade sold:"))

total = 0

if season == "summer":
    total = (small *(2.0 - 1.0) + medium*(2.5-1.25)+large*(3.0-1.5))
    print("Total profit for the day in the summer : $", total, sep = "")
elif season == "other":
    total = (small *(1.5 - 0.75) + medium*(2.0-1.0)+large*(2.5-1.25))
    print("Total profit for the day in the rest of the year : $", total, sep = "")
    

    