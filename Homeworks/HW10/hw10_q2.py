"""
Author: [Anthony Lamelas]
Assignment / Part: HW10 - Q2
Date due: April 18, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""
#Sorry, I know there has to be a more efficient way to do this but this is what I got.

def get_ordinal(word):
    ord_total = 0
    for char in word:
        ord_total += ord(char)
    return ord_total

def group_anagrams(path):
    try:
        list_words = []
        with open(path, 'r') as file:
            for line in file:
                word = line.strip()
                list_words.append(word)

        anagrams = []
        not_anagrams = []
        i = 0
        length = len(list_words)

        while i < length:
            iword = list_words[i]
            ana_list = [iword]
            j = i + 1  
            found_anagram = False  
            while j < length:
                jword = list_words[j]
                if get_ordinal(iword) == get_ordinal(jword):
                    ana_list.append(jword)
                    list_words.pop(j)
                    length -= 1  
                    found_anagram = True  
                else:
                    j += 1  

            if not found_anagram:
                not_anagrams.append(iword)
                i += 1  
            else:
                if len(ana_list) > 1:
                    anagrams.append(ana_list)

        
        if not_anagrams:
            anagrams.append([not_anagrams.pop()])  

        return anagrams

    except FileNotFoundError:
        print("Unable to read the file. Please check the file path.")
        return None

anagrams = group_anagrams("hw_text1.txt")
print(anagrams)

