"""
Author: [Anthony Lamelas]
Assignment / Part: HW4 - Q1 
Date due: February 22, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""


batches = 0
mochiko = int(input("Enter an amount (g) of mochiko: "))
sugar = int(input("Enter an amount (g) of sugar: "))
cornstarch = int(input("Enter an amount (g) of cornstarch: "))
anko = int(input("Enter an amount (g) of anko: "))


cup_mochiko = mochiko / 220.0
cup_sugar = sugar / 220.0
cup_cornstarch = cornstarch / 220.0
cup_anko = anko / 220.0

while cup_mochiko > 3 and cup_sugar > 1.5 and cup_cornstarch > 2 and cup_anko > 1:
    batches += 1
    cup_mochiko -= 3
    cup_sugar -= 1.5
    cup_cornstarch -= 2
    cup_anko -= 1




print("With this amount of ingredients, you can make", batches, "batch(es) of 24 mochi.")
