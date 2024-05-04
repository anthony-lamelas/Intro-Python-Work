"""
a
10
11
12
13
14
15
16
17
18
19
20

b
3
5
7
9
11

c
63
56
49
42
35

d
1
3
9
27

e
fizz
14
fizz
16
fizz
18
fizz
20
fizz
22

"""


print("This is a four operation calculator")
question = str(input("Hit enter to continue and Q to quit calculator: "))

while question != "Q":
       
    number = float(input("Enter your first number:"))
    operation = str(input("Enter the operation (+, -, *, /):"))
    second_number = float(input("Enter your second number:"))


    
    if operation == "+":
        print(number, operation, second_number, "=", number + second_number)
    elif operation == "-":
        print(number, operation, second_number, "=", number - second_number)
    elif operation == "*":
        print(number, operation, second_number, "=", number * second_number)
    elif operation == "/" and second_number != 0:
        print(number, operation, second_number, "=", number / second_number)
    elif operation == "/" and second_number == 0:
        print("INVALID")
    elif operation == "/" or operation != "-" or operation != "+" or operation != "*":
        print("INVALID")
        
    question = str(input("Hit enter to continue and Q to quit calculator: "))


    