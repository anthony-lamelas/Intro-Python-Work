message = str(input("Please enter your message: "))
count = 0
vowels = "aeiouAEIOU"
new_message = message.replace(" ", "")
length = len(new_message)

for i in range(0, length): 
    if new_message[i] not in vowels:
        count += 1

        
print("Total number of consonants: ", count)



