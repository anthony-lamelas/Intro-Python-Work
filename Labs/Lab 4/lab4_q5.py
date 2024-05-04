length = int(input("Python needs to tell you a secret. How many characters wide can its message be? "))
for i in range(1, length+1):
    
    line = ""
    for j in range(1,length + 1):
        if i ==j or i +j == length + 1: 
            line += "X"
        else:
            line += "X"
    print(line)
    
    
for i in range (1, length+1):
    line=""
    for j in range (1, length + 1):
        if i ==1:
            if j ==1:
                line += " "
            elif length >j:
                line += "O"
            elif length == j:
                line += " "
        
        elif length > i:
            if j==1:
                line += "O"
            elif length > j:
                line += " "
            elif length == j:
                line += "O"
                
        elif length == i:
            if j ==1:
                line += " "
            elif length > j:
                line += "O"
            elif length == j:
                line += " "
    print(line)
    
    
for i in range(1, length + 1):
    line = ""
    for j in range(1,length + 1):
        if i ==j or i +j == length + 1: 
            line += "X"
        else:
            line += "X"
    print(line)
        
                
                
