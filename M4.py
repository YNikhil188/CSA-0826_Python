def calculate_grade(average_marks):
    if average_marks >=90:
        return 'A'
    elif average_marks >=80:
        return 'B'
    elif average_marks >=70:
        return 'C'
    elif average_marks >=60:
        return 'D'
    elif average_marks >=50:
        return 'E'
    else:
        return 'FAIL'
num_sub=int(input("enter the no of subjects:"))
total_marks=0
for i in range (num_sub):
    marks=input(f"enter the marks{i+1}:")
    total_marks+=int(marks)
average_marks=total_marks//num_sub
grade=calculate_grade(average_marks)
print("grade of student:",grade)