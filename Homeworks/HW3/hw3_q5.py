"""
Author: [Anthony Lamelas]
Assignment / Part: HW3 - Q5 
Date due: February 15, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""
import random

max_hp = int(input("Enther the max health of this Pokémon: "))

current_hp = random.randrange(1, max_hp+1)
ball = random.randrange(0,256)
rand_number = random.randrange(0,256)

f = (max_hp *255*4)/(current_hp *ball)

if ball == 0:
     print("Oh no! The Pokémon broke free!")
elif f < rand_number:
    print("Oh no! The Pokémon broke free!")
elif f >= rand_number:
    print("You've caught the Pokémon!")
    

