def my_func(w):
    total = 0
    for c in w:
        total += ord(c)
    return total


with open ('words_alpha.txt') as file:
    
    data =[word.strip() for word in file]
    
data_dict = {value : (len(value), my_func(value)) for value in data}
    

print(data_dict)


