def decode(string: str, start: int, end: int, N:int):
    store=""
    for i in range(1, len(string)-1, N):
        store+= string[i]
    return(store)

def decode_entire_msg(code: str):
    store1=0
    store2=0
    counter = 0
    encoded=""
    
    
    while counter < 101:
        if code[counter].isdigit():
            store1= counter
            count= counter+1
            while not code[count].isdigit():
                count += 1
            store2 = count
            encoded += decode(code[store1:store2+1], store1, store2, int(code[counter]))
        counter += 1
            
    return(encoded)


def decode_roman_file(ROMAN_FILE, ROMAN_DECODED_FILE):
    with open(ROMAN_DECODED_FILE) as outfile:
        with open(ROMAN_FILE) as file:
            for line in file:
                temp += file.readline()
        
                message = outfile.write(temp)
                
    return decode_entire_msg(message)


def main():
    ROMAN_FILE = "roman_code_msg.txt"
    ROMAN_DECODED_FILE = "secret_msg.txt"
    decode_roman_file(ROMAN_FILE, ROMAN_DECODED_FILE)
                
                
        
        
        
        