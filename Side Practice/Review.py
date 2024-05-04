#binary, hex, octal
#Pemdas
#not, and, or

"""
.read returns file as a string
.readline returns next line of the file including /n STRIP this to remove /n
.readlines returns a line of strings

"""

def binary_convert(n):
    binary =""
    power = 0
    
    while n >= 2**power:
        power += 1
    power -= 1
    
    while power >= 0:
        
        if n >= 2 ** power:
            binary += "1"
            n -= 2**(power)
        else:
            binary += "0"
        power -= 1
        
    return binary
     


def count_words(path):
    try:
        with open(path, 'r') as file:
            dictionary = {}
            lines = file.readlines()
            
            for line in lines:
                words = line.split()
                for word in words:
                    if word not in dictionary:
                        dictionary[word] = 1
                    else:
                        dictionary[word] += 1
                    
        return dictionary
    
    except FileNotFoundError:
        print("File not found")

print(count_words("hw_text1.txt"))
            






