# The constants are numbers 3 and 4.


# 1 is a string, 2 is a float, 3 is an int, 4 is an int, and 5 is a boolean.

amount = int(input("Enter the number of scones you want to make:"))
             
salted_butter = amount*7.5
flour = amount*35
milk = amount*15

cups_butter = (salted_butter / 75.0) / 3
cups_flour = flour / 150.0
cups_milk = (milk / 100.0) / 2

print("To make", amount, "scones use", cups_butter,"cups butter", cups_flour, "cups flour, and", cups_milk, "cups milk")
             