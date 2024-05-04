string = str(input("Enter a string to be printed (in the format [text]-[text] ...): "))
print("Printing: ")
store = ""
for letter in string:
    if letter != "-":
        store += letter
    else:
        print(store)
        store = ""
        
print(store)
        
        