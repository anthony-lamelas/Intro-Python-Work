base = float(input("Please enter a positive integer to serve as the base: "))
power = float(input("Please enter a positive integer to serve as the highest power: "))




if base < 0 or power < 0:
    print(" Both values must be POSITIVE INTEGERS.")
    
    
elif base%1 !=0 or power%1 != 0:
    print(" Both values must be POSITIVE INTEGERS.")
    
else:
    for i in range(0,int(power)+1):
        print (int((base ** i)))
