stu_list = {}

with open ("nyu_students.csv", 'r') as file:
    lines = file.read().split(",")
    
    for i in lines:
        stu_N = lines[0]
        
        if stu_N not in stu_list:
            stu_first= i[1]
            stu_last = i[2]
            stu_email = i[3]
            stu_gpa = i[4]
            stu_grad = i[5]
            stu_street = i[6]
            stu_postal = i[7]
        
            temp = {}
            temp['first_name'] = stu_first
            temp['last_name'] = stu_last
            temp['email'] = stu_email
            temp['gpa'] = stu_gpa
            temp['grad_year'] = stu_grad
            temp['street'] = stu_street
            temp['postal_code'] = stu_postal
        
    
            result[stu_name] = temp