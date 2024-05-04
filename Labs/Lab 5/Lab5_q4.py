wage = 12.25

hours = 45
total = 0
    
if hours > 40:
    total = 40*wage
    hours -= 40
    total += hours*(1.5*wage) 
elif hours<= 40:
    total = hours*wage 
    
print(0.7*(total))
        
        
