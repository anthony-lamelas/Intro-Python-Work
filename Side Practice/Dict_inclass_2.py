def convert_grades_to_dictionary(data):
    result = {}
    
    for student in data:
        stu_name = student[0]
        
        if stu_name not in result:
            stu_netid = student[1]
            stu_midterm = student[2]
            stu_final = student[3]
        
            temp = {}
            temp['NetID'] = stu_netid
            temp['Midterm Grade'] = stu_midterm
            temp['Final Grade'] = stu_final
        
    
            result[stu_name] = temp
    return result
 




grades_list = [["Emily Kaldwin", "ek12345", 88, 90], ["Sakura Kinomoto", "sk12345", 98, 98], ["Maximilien Robespierre", "mr12345",
76, 89], ["Emily Kaldwin", "ek12345", 100, 100]]
grades_dictionary = convert_grades_to_dictionary(grades_list)
print(grades_dictionary["Sakura Kinomoto"]["NetID"]) # prints
"sk12345"
print(grades_dictionary["Emily Kaldwin"]["Midterm Grade"]) # prints
"88"
print(grades_dictionary["Maximilien Robespierre"]["Final Grade"]) #prints "89"
