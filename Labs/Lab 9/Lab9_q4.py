import random

def shuffle_create(lst):
    
    original = lst[:]
    shuffle = []
     
    while len(original) > 0:
        index = random.randrange(0,len(original))
        shuffle.append(original[index])
        original.pop(index)
    
    return shuffle
    
    
def shuffle_in_place(lst):
    
    for i in range (len(lst)-1, -1, -1):
        rand = random.randint(0, i)
        
        lst[i], lst[rand] = lst[rand], lst[i]
    
    
    
    
    
def main():
    list_one = ["Jean Valjean", "Javert", "Fantine", "Cosette", "Marius Pontmercy","Eponine", "Enjolras"]
    print("ORIGINAL LIST_ONE: {}".format(list_one))
    # First function execution
    print("LIST CREATED BY SHUFFLE_CREATE: {}\n".format(shuffle_create(list_one)))
    
    list_two = ["A", 0, 0, 5, 1, 3, 2]
    print("ORIGINAL LIST_TWO: {}".format(list_two))
    # Second function execution
    shuffle_in_place(list_two)
    print("LIST_TWO AFTER SHUFFLE_IN_PLACE: {}".format(list_two))
    
    
main()
