"""
Author: [Anthony Lamelas]
Assignment / Part: HW10 - Q1 
Date due: April 18, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""

def group_students(spec, pref):
    
    club_list = []
    length = len(spec)
    
    for index in range(length):
        club_list.append([])
        
    
    for (student, club) in pref:
        for i in range(length):
            spec_club, count = spec[i]
            if club == spec_club and count > 0:
                club_list[i].append(student)
                spec[i] = (spec_club, count - 1)
                
                
    return club_list
    

#Example Usage
club_specs = [("Chess Club", 15), ("Art Club", 20), ("Writing Club", 3)]

student_prefs = [
("Alice", "Chess Club"),
("Bob", "Chess Club"),
("Flora", "Writing Club"),
("Charlie", "Art Club"),
("David", "Writing Club"),
("Melody", "Writing Club"),
("Ana", "Writing Club")
]

print(group_students(club_specs, student_prefs))