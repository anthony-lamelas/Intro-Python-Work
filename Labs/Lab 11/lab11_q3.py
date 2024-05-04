def count_vowels(path):
    try:
        with open(path, 'r') as file:
            text = file.read().upper()  
            vowels = ['A','E','I','O','U']
            
            
            
            positive_vowels = {i: text.count(i) for i in vowels}
            return positive_vowels

    except FileNotFoundError:
        print("File not found:", path)

        
        
def main():
    
    print(count_vowels("hw_text1.txt"))
    
    
main()