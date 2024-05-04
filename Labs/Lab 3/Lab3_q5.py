amount = int(input("Please enter how many positive values you want to consider: "))
print("Enter your values:")
temp = 0
for i in range(1,amount +1):
    value = float(input(""))
    if value < 0:
        print("ERROR")
    elif value > temp:
        temp = value
        
print("The largest of these values is", temp)


     
    
    



