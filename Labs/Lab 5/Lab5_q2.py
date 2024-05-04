'''
answer = str(input("Enter your phrase: "))

print(answer[len(answer)-1::-1])
'''


answer = str(input("Enter your phrase: "))
length = len(answer)

temp = ""

for i in range (1,length+1):
    temp += answer[-i]
    
print(temp)

