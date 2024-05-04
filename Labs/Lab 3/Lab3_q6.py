import random

print("Welcome to Blackjack!")

d_sum = random.randrange(2,22)
sum = random.randrange(1,12)
print(" Your current card sum is: ", sum)
next = str(input("What would you like to do next?: (DEAL, STAND)"))



while sum < 22 and next == "DEAL":
    
    sum = sum + random.randrange(1,12)
    print(" Your current card sum is: ", sum)
    next = str(input("What would you like to do next?: (DEAL, STAND)"))
    
if next == "STAND":
    if sum == d_sum:
        print("You tied! Your card some was", sum, "and the dealer's was", d_sum)
    elif sum > d_sum:
        print("You won! Your car sum was,", sum, "and the dealer's was", d_sum)
    elif sum < d_sum:
        print("You lost! Your car sum was,", sum, "and the dealer's was", d_sum)
        
if sum > 21:
    print("You lost! Your card sum was", "and the dealer's was", d_sum)
        
    
