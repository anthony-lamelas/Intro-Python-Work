my_dict = {"a": 15 , "c": 35 , "b": 20}

print("Keys:")
for key in my_dict.keys():
    print(key, end=" ")
    
print()
print()
print("Values:")

for value in my_dict.values():
    print(value, end=" ")
    
print()
print()
print("Both:")

for key, value in my_dict.items():
    print(key, value)
    
print()
print("Sorted:")

for key in sorted(my_dict.keys()):
    print(key, my_dict[key])

