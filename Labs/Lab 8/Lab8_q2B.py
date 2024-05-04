def squared_numbers(filename, outFile):
    temp = 0
    with open(filename) as file:
        with open(outFile, 'w') as outFile:
            for i in file:
                temp = int(i.strip())
                outFile.write(temp**2 + '\n')
                temp = 0
                
                
def main():
    squared_numbers("nums2.txt", "squaredNumbers.txt")
            
