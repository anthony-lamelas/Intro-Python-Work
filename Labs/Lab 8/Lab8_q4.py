def get_last_char(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1]
            return last_line.strip()
        else:
            return None
        
        
def alphabet_soup(filename):
    
    letter = ord(get_last_char(filename))
    
    with open(filename, 'w') as file:
        while letter < 122:
            file.write(chr(letter+1) + '\n')
            letter += 1
        
    
    
    
    
    
        
        
