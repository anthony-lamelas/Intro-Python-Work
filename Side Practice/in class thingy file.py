def get_input():
    
    number = int(input("Enter a number: "))
    
    if number >= 500 and number <= 100:
        return number
    
    else:
        raise Exception("Number out of range: " + str(value))
    
def main():
    
    try:
        result = get_input()
        
    
    except Exception as eee:
        print(eee)
        
    print(result)
        
        


if __name__=="__main__":
    main()
    

