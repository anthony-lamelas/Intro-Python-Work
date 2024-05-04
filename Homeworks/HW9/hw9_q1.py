"""
Author: [Anthony Lamelas]
Assignment / Part: HW9 - Q1 
Date due: April 11, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""


def update_frequencies(lst, str):
    new_freq = []
    
    first_tup = lst[0]
    second_tup = lst[1]
    third_tup = lst[2]
    fourth_tup = lst[3]
    
    acount = str.count('A')
    ccount = str.count('C')
    tcount = str.count('T')
    gcount = str.count('G')
    
    new_freq = [("A",acount + first_tup[1]), ("C",ccount + second_tup[1]), ("T",tcount + third_tup[1]), ("G",gcount + fourth_tup[1])]
    
    return (f"Number of nucleotides added: A -> {acount} | C -> {ccount} | T -> {tcount} | G -> {gcount} \n{new_freq}")
   
    
    
def main():
    old_frequencies = [("A", 20), ("C", 23), ("T", 125), ("G", 4)]
    new_sequence = "ACCCGTTA"
    new_frequencies = update_frequencies(old_frequencies, new_sequence)
    print(new_frequencies)
main()
