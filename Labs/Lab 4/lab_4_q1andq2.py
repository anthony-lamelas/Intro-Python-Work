"""
a:
0 0 0 0
0 1 2 3 
0 2 4 6
0 3 6 9

b:
0 1
0 2
0 3
0 4
1 2
1 3
1 4
2 3
2 4
3 4

c:
2 4 6 8
4 6 8
6 8
8

d:
0
0 2
0 2 4
0 2 4 6


"""

product = 0

play = str(input("Press ENTER to calculate a product or Q to quit:"))
while play != "Q":
    first_factor = int(input("Please input your first factor: "))
    second_factor = int(input("Please enter your second factor: "))
    
    if first_factor < 1 or second_factor < 1:
        print("ERROR: Positive integers must be entered.")
    else:
        for i in range(1, second_factor + 1):
            product += first_factor
        print("Your product is:", product)
    
    play = str(input("Press ENTER to calculate a product or Q to quit:"))
    
    






