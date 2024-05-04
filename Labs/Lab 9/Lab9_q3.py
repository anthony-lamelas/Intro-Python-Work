import random

def get_random_word(filepath):
    try:
        temp = []
        with open (filepath, 'r') as file:
            text = file.readlines()
            for line in text:
                words = line.split()
                for word in words:
                    temp.append(word.strip())
            
        return random.choice(temp)
            
    
    except FileNotFoundError:
        print("File not found:", filepath)
    
    
    
    
    
    

    
def main():
    print(get_random_word("hw_text1.txt"))
if __name__ == '__main__':
    main()
