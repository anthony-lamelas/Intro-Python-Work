"""
Author: [Anthony Lamelas]
Assignment / Part: HW7 - Q1 
Date due: March 14, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""

def calculate_grade(assignment_score, midterm_score, final_score):
    grade = (0.4*assignment_score) + (0.3*midterm_score ) + (0.3*final_score)
    return grade
    
    
def get_valid_score(prompt):
    score = input(f"Enter a score for {prompt}: ")
    
    while  not score.isdigit() or float(score) < 0 or float(score) > 100:
        print("Invalid, Enter a numeric value between 0 and 100.")
        score = input(f"Enter a score for {prompt}: ")

    return float(score)
    
    
    
    
    
    
def display_result(grade):
    print("Grade:",grade,".",sep="",end=" ")
    if grade >= 90:
        print("Outstanding performance")
    elif grade >= 80 and grade < 90:
        print("Good work")
    elif grade >= 70 and grade < 80:
        print("Can improve")
    elif grade >= 60 and grade < 70:
        print("Passed")
    else:
        print("Failed")
    
    

 

assignment_score = get_valid_score("Assignments")
midterm_score = get_valid_score("Midterm")
final_score = get_valid_score("Final")
calculated_grade = calculate_grade(assignment_score, midterm_score, final_score)
display_result(calculated_grade)
    
