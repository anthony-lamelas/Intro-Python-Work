"""
Author: [Anthony Lamelas]
Assignment / Part: HW3 - Q3
Date due: February 15, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""

xp = float(input("Enter this user's current XP: "))

if xp > 60:
    print("ERROR: Please enter a valid XP value.")
elif xp >= 40 and xp <= 60:
    print("Level 5 Plater (XP: ", xp, ")")
elif xp >= 30 and xp <= 39.9:
    print("Level 4 Plater (XP: ", xp, ")")
elif xp >= 25 and xp <= 29.9:
    print("Level 3 Plater (XP: ", xp, ")")
elif xp >= 15 and xp <= 24.9:
    print("Level 2 Plater (XP: ", xp, ")")
elif xp < 15:
    print("Level 1 Plater (XP: ", xp, ")")
    