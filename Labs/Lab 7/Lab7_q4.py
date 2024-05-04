def prompt_user_for_pw():
    password = input("Please create a password:")
    
    return password


def is_strong_pw(pw: str):
    
    length = 0
    special = 0
    upper = 0
    lower = 0
    number = 0
    
    if len(pw) >= 8:
        length = 1
    
    for char in pw:
        if char.isdigit():
            number = 1
        if char.isupper():
            upper = 1
        if char.islower():
            lower = 1
        if char in "!@#*":
            special = 1
        
            
        
    if length + special + upper + lower + number == 5:
        return True
    else:
        return False
        
        
        
def main():
    
    password = prompt_user_for_pw()
    strong = is_strong_pw(password)
    
        
    if strong == True:
        print("Thank you! Your password is considered strong.")
        
    while strong == False:
        print("Password too weak! Strong passwords must be greater than or")
        print("equal to 8 characters in length, contain at least 1 special")
        print('character from the following: "!", "@", "#", "*" contain at')
        print("least 1 uppercase character, contain at least 1 lowercase")
        print("character, and contain at least 1 number")
        password = prompt_user_for_pw()
        strong = is_strong_pw(password)
        
    if strong == True:
        print("Thank you! Your password is considered strong.")
        
        
    
    
main()
    
        