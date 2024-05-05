def countdown(n):
    if n == 0:
        print("Done!")
    else:
        print(n)
        countdown(n + 1)
        
        
print(countdown(3))


#This is wrong, n+1 should be n-1