def decreasing_numbers(filename, n):
    with open(filename, 'w') as file:
        for i in range (n, 0, -1):
            file.write(str(i) + '\n')
            
            

def main():
    decreasing_numbers("nums.txt", 5)
            