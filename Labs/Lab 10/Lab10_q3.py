def count_vowels(path):
    try:
        with open(path, 'r') as file:
            text = file.read().upper()  
            vowels = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
            positive_vowels = {}

            for vowel in vowels.keys():
                count = text.count(vowel)
                
                if count > 0:
                    positive_vowels[vowel] = count

            return positive_vowels

    except FileNotFoundError:
        print("File not found:", path)

        
        
def main():
    
    print(count_vowels("hw_text1.txt"))
    
    
main()
        
        
        
        
        
        
        
        