"""
Author: [Anthony Lamelas]
Assignment / Part: HW4 - Q2
Date due: February 22, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""


value = 0
max_value = 0
winner = ""

players = int(input("How many players played this round?"))
while players < 1:
    print("Invalid input.")
    players = int(input("How many players played this round?"))
      
    
for i in range(1,players+1):
    temp = (input("Enter the value of a property/asset, or DONE to finish: "))
    while temp != "DONE":
        value += float(temp)
        temp = (input("Enter the value of a property/asset, or DONE to finish: "))
    
    print("Player ", i, " has ", round(value,2), " dollars.", sep = "")
    
    
    
    
    if value > max_value:
        max_value = value
        winner = str(i)
        round(max_value,2)
    
    value = 0

print("Congratulations, player ", winner, "! You won with $", max_value, "!", sep = "")
    
    
    
    
    
    
    
    
    
        
        