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
    
    
        
def main():
    secret = "3Gn.olwo pd/Q gh5l!d pulAk c_kosk an2 moPn! .y\oausr? 3mqei,sd+ktcbe.KrkcmOpsne!se odYpqo>kulq fag pozrtks dftpqh /ipaslk!dp4vm fkofwolp9 mjcnre"
    message=decode_entire_msg(secret)
    print(message)

if __name__=="__main__":
    main()
