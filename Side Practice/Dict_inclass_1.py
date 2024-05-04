import random




rand_dict = {}

for i in range (1,1001):
    rand_dict.update({i:random.randrange(1,501)})
    
    
print(rand_dict)

count_dict = {}


for value in rand_dict.values():
    if value in count_dict:
        count_dict[value] += 1
    else:
        count_dict[value] = 1

print(count_dict)

    
