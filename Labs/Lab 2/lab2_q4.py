highest_exam = int(input("Enter your highest exam grade:"))
middle_exam = int(input("Enter your second highest exam grade:"))
lowest_exam = int(input("Enter your third highest exam grade:"))
avg_hw = int(input("Enter your average homework grade: "))
avg_lab = int(input("Enter your average lab grade:"))


total = (highest_exam*.25)+(middle_exam*.20)+(lowest_exam*.15)+(avg_hw*.20)+(avg_lab*.20)
print(total)


if total > 92:
    print("Your final grade is A")
elif total >=90 and total <= 92:
        print("Your final grade is A-")
elif total >= 87 and total < 90:
        print("Your final grade is B+")
elif total >= 83 and total < 87:
        print("Your final grade is B")
elif total >= 80 and total < 83:
        print("Your final grade is B-")
elif total >= 77 and total < 80:
        print("Your final grade is C+")
elif total >= 73 and total < 77:
        print("Your final grade is C")
elif total >= 70 and total < 73:
        print("Your final grade is C-")
elif total >= 67 and total < 70:
        print("Your final grade is D+")
elif total >= 60 and total < 67:
        print("Your final grade is D")
elif total < 60:
        print("Your final grade is F")






