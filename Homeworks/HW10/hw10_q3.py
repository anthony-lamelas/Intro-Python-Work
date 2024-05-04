"""
Author: [Anthony Lamelas]
Assignment / Part: HW10 - Q3
Date due: April 18, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""



def word_frequency_counter_from_file(path):
    try:
        count_words = {}
        line_index = 0
        
        with open(path, 'r') as file:
            lines = file.readlines()
            
            for line in lines:
                line = line.strip().split()
                word_index = 0
                
                for word in line:
                    if word in count_words:
                        count, indexes = count_words[word]
                        count += 1
                        indexes.append( word_index)
                        count_words[word] = (count, indexes)
                    else:
                        count_words[word] = (1, [ word_index])
                    
                    word_index += 1
                
                line_index += 1
        
        return count_words
    except FileNotFoundError:
        print("Unable to read the file. Please check the file path.")
        return None

invalid_word_stats = word_frequency_counter_from_file("invalid_file.txt")
print(invalid_word_stats)

sample_word_stats = word_frequency_counter_from_file("hw_text1.txt")
print(sample_word_stats)
