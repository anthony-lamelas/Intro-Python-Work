
total = 1
temp = 0

print(" Welcome to the Factorial Factory!")
amount = int(input("Please enter the amount of factorials that you would like to calculate: "))

while amount < 1:
    print("ERROR: Please enter a positive amount")
    amount = int(input("Please enter the amount of factorials that you would like to calculate: "))

for i in range(1, amount + 1):
    factorial = int(input("Please enter a positive integer : "))
    while amount < 0:
        print("ERROR: Please enter a positive integer")
        factorial = int(input("Please enter a positive integer : "))
    for j in range(factorial, 0, -1):
        temp = j
        total *= temp
    print(factorial, "! is eaqual to ", total, sep = "")
    total = 1