"""
Author: [Anthony Lamelas]
Assignment / Part: HW8 - Q1 
Date due: April 04, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""

def find_longest_word_in_file(str):
    long_word = ""
    current_word = ""
    try:
        
        with open(str, 'r') as file:
            char = file.read(1)
            while char != "":
                if char.isalpha():
                    current_word += char
                else:
                    if len(current_word) > len(long_word):
                        long_word = current_word
                    current_word = ""
                char = file.read(1)
        if len(current_word) > len(long_word):
            long_word = current_word
            
    except FileNotFoundError:
        print("File not found:", str)
        
    return long_word
            

            
def replace_substr_in_file(path: str, target_substr:str, replacement_word: str):
    try:
        with open (path, 'r') as file:
            text = file.read()
            new_text = text.replace(target_substr, replacement_word)
        with open (path, 'w') as file:
            file.write(new_text)
    except FileNotFoundError:
        print("File not found:", path)
        
        
def count_word_occurrences_in_file(file_path, target_word):
    try:
        with open (file_path, 'r') as file:
                text = file.read()
                current_word = ""
                count = 0
                for char in text:
                    if char.isalpha():
                        current_word += char
                    else:
                        if current_word == target_word:
                            count += 1
                        current_word = ""
                if current_word == target_word:
                    count += 1
        return count
    
    except FileNotFoundError:
        print("File not found:", file_path)
    
def main():
  
    input_file = "hw_text1.txt"
    print(f"Longest word in the file: {find_longest_word_in_file(input_file)}")
    target_substr = "test"
    replacement_word = "exam"
    replace_substr_in_file(input_file, target_substr, replacement_word)
    print(f'Replaced "{target_substr}" with "{replacement_word}" in the file.')
    word_to_count = "exam"
    word_occurrences = count_word_occurrences_in_file(input_file, word_to_count)
    print(f'Occurrences of "{word_to_count}" in the file: {word_occurrences}')
    
main()
            
    
                
        
                