"""
Author: [Anthony Lamelas]
Assignment / Part: HW8 - Q2
Date due: April 04, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""

def get_word_count(path):
    try:
        with open (path, 'r') as file:
            text = file.read()
            word = False
            count = 0
            
            for char in text:
                if char.isalpha() and not word:
                    count += 1
                    word = True
                elif not char.isalpha():
                    word = False
               
            if text[-1].isalpha():
                count += 1
                    
                        
        return count
    
    except FileNotFoundError:
        print("File not found:", path)
        
def main():
    count = get_word_count("hw_text1.txt")
    print(f"This file has {count} word(s).")
main()