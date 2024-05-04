"""
hhhhheeeeellllllllllooooo

//

10
whoop
15
10
whoop
18
20

"""

def numberify(word):
    
    word = word.upper()
    
    for char in word:
        if char == "A":
            word = word.replace("A","4")
        
        elif char == "E":
            word = word.replace("E","3")
            
        elif char == "I":
            word = word.replace("I","1")
            
        elif char == "S":
            word = word.replace("S","5")
        
        elif char == "T":
            word = word.replace("T","7")
        
        elif char == "O":
            word = word.replace("O","0")
            
    return word


def main():
    message = input("Please enter a message to numberify: ")
    print("Your numberified string is:",numberify(message))

main()
        

