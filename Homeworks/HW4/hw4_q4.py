"""
Author: [Anthony Lamelas]
Assignment / Part: HW4 - Q4 
Date due: February 22, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""
import random

card_one = random.randrange(1,12)
card_two = random.randrange(1,12)
card_three = random.randrange(1,12)

dealer_card = random.randrange(0,101)
while dealer_card < 3 or dealer_card > 33:
    dealer_card = random.randrange(0,101)
    
    

play = str(input("Would you like to play 'Twenty-One? [y/n] "))

while play != "y" and play != "n":
    
     play = str(input("Would you like to play 'Twenty-One? [y/n] "))
    
    
if play == "n":
    print("Thank you for playing!")
elif play == "y":
    print("Your cards are worth ", card_one, " and ", card_two, ".",sep="")
    next_card = str(input("Would you like another card? [y/n] "))
    
    while next_card != "y" and next_card != "n":
        next_card = str(input("Would you like another card? [y/n] "))
        
    if next_card == "y":
        print("Your score is ", card_one + card_two + card_three, "!", sep="")
        print("Your opponent's score is ", dealer_card, "!", sep="")
        
        
        if card_one + card_two + card_three > 21 and dealer_card > 21:
            print("It's a draw!")
        elif card_one + card_two + card_three > dealer_card or card_one + card_two + card_three == 21 or dealer_card > 21:
            print("You win! Your score was ", card_one + card_two + card_three, ".", sep="")
        elif card_one + card_two + card_three< dealer_card or dealer_card ==21 or card_one + card_two + card_three > 21:
            print("Your opponent wins! Their score was ", dealer_card, ".", sep="")
        else:
            print("It's a draw!")
    
    elif next_card == "n":
        print("Your score is ", card_one + card_two, "!", sep="")
        print("Your opponent's score is ", dealer_card, "!", sep="")
        if card_one + card_two > 21 and dealer_card > 21:
            print("It's a draw!")
        elif card_one + card_two > dealer_card or dealer_card >21 or card_one +card_two == 21:
            print("You win! Your score was ", card_one + card_two, ".", sep="")
        elif card_one + card_two < dealer_card or card_one + card_two > 21:
            print("Your opponent wins! Their score was ", dealer_card, ".", sep="")
        else:
            print("It's a draw!")
                        
                        
                        
                        
   
                        
        
 
       
    
    
    
    
    
    
    