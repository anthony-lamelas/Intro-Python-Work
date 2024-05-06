def reading_file_data():
    try:
        with open ("student.txt",'r') as file:
            lines = file.readlines()
            dict = {}
            for line in lines:
                fields =line.strip().split(",")
                dict.update({fields[0]:{"first_name":fields[1], "last_name":fields[2], "gpa":fields[3], "grad_year":fields[4]}})
            return dict
                        
    except FileNotFoundError:
        print("Print file not found.")
        
print(reading_file_data())