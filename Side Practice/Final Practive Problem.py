class Student:
    def __init__(self, gpa, course_list=None):
        self.gpa = gpa
        self.course_list = course_list if course_list is not None else []
        for course in self.course_list:
            if self not in course.student_list:
                course.add_student(self)

    def __str__(self):
        return f"Student GPA: {self.gpa}, Courses: {[course for course in self.course_list]}"

    def add_course(self, course):
        if course not in self.course_list:
            self.course_list.append(course)
            if self not in course.student_list:
                course.add_student(self)
        else:
            print("Course is already in the course list.")

    def drop_course(self, course):
        if course in self.course_list:
            self.course_list.remove(course)
            if self in course.student_list:
                course.drop_student(self)
        else:
            raise Exception("Course is not in the course list.")

class Course:
    def __init__(self, student_list=None):
        self.student_list = student_list if student_list is not None else []
        for student in self.student_list:
            if self not in student.course_list:
                student.add_course(self)

    def __str__(self):
        students_info = ", ".join([f"GPA: {student.gpa}" for student in self.student_list])
        return f"Course Students: {len(self.student_list)}, Students: [{students_info}]"

    def add_student(self, student):
        if student not in self.student_list:
            self.student_list.append(student)
            if self not in student.course_list:
                student.add_course(self)
        else:
            print("Student is already in the student list.")

    def drop_student(self, student):
        if student in self.student_list:
            self.student_list.remove(student)
            if self in student.course_list:
                student.drop_course(self)
        else:
            raise Exception("Student is not in the student list.")

    def average_gpa(self):
        total = 0
        length = len(self.student_list)
        for student in self.student_list:
            total += student.gpa

        return total / length

def main():
    Physics = Course()
    CS = Course()
    George = Student(999, [CS])
    Math = Course([George])
    Valentine = Student(3.9)
    Me = Student(3.8, [CS, Physics])

    Me.add_course(Math)

    print(Physics)
    print(Math)
    print(George)
    print(Math)
    print(Valentine)
    print(Me)

main()

