"""
Author: [Anthony Lamelas]
Assignment / Part: HW8 - Q3 
Date due: April 04, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""


def create_error_log(seq, path):
    try:
        seq_length = len(seq)
        count = 1  
        with open('error_log.txt', 'w') as outfile:
            with open(path, 'r') as file:
                for line in file:  
                    line = line.strip()  
                    if not line.isdigit():
                        outfile.write(f"IndexError at LINE {count}: The value read {line} is larger than the sequence length of {seq_length}.\n")
                    elif int(line) >= seq_length:
                        outfile.write(f"ValueError at LINE {count}: The value read {line} cannot be casted into an integer to be used as an index.\n")
                    count += 1  
            
    except FileNotFoundError:
        with open('error_log.txt', 'a') as outfile:
            outfile.write("The file specified was not found or could not be opened.\n")

def main():
    create_error_log("ACTGC AXT", 'hw_text1.txt')

main()
