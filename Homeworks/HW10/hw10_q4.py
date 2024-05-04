"""
Author: [Anthony Lamelas]
Assignment / Part: HW10 - Q4
Date due: April 18, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""

def merge_intervals(intervals):
    
    new_inter = [intervals[0]]
    length = len(intervals)
    
    for i in intervals[1:]:
        if i[0] <= new_inter[-1][1]:
            new_inter[-1] = (new_inter[-1][0], i[1])
            
        else:
            new_inter.append(i)

    return new_inter
        

#Example Usages
print(merge_intervals([(1, 3), (2, 6), (8, 10), (15, 18)]))

print(merge_intervals([(1, 4), (4, 5)]))
        