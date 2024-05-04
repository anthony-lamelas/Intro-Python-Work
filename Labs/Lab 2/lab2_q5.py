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