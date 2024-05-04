import math

def approximate_pi(num_terms):
    
    pi = 1
    y = 3
    count = 1
    
    for x in range(1,num_terms+1):
        
        if count % 2 != 0:
            pi -= 1/(y*(3**x))
            
        elif count % 2 == 0:
            pi += 1/(y*(3**x))
        
        y += 2
        count += 1
        
    return pi * math.sqrt(12)
        
print(approximate_pi(120))
        
        
