"""
Author: [Your name here]
Assignment / Part: HW1 - Q1 (etc.)
Date due: February 01, 11:59pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of Engineering
Policies and Procedures on Academic Misconduct.
"""
quarters=int(input("Number of quarters:"))
qvalue=quarters*0.25
dimes=int(input("Number of dimes:"))
dvalue=dimes*0.1
nickels=int(input("Number of nickels:"))
nvalue=nickels*0.05
pennies=int(input("Number of pennies:"))
pvalue=pennies*0.01

total = qvalue+dvalue+nvalue+pvalue

dollars = total//1
cents = int((total-dollars)*100+0.5)

print("The total is", dollars, "dollar(s) and", cents, "cent(s)") 



    
    



