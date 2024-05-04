user_input = input("Please enter your message: ")
secret_message = ""
capitalize_next = True

for i in user_input:
    if i.isupper() and capitalize_next:
        secret_message += i
        capitalize_next = False
    elif i == " ":
        capitalize_next = True

print("Your secret message is:", secret_message)



'''
user_input = input("Please enter your message: ")
secret_message = ""
save_next = False

for char in user_input:
    if char.isupper() and not save_next:
        secret_message += char
        save_next = True
    elif char.islower() and save_next:
        secret_message += char
    else:
        save_next = False

print("Your secret message is:", secret_message)





'''



