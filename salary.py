# Enter the salary and grade of the employee
salary = float(input("Enter the salary: "))
grade = input("Enter the grade (A or B): ")
# Calculate the bonus based on the grade
if grade == 'A':
    bonus_percent = 5
elif grade == 'B':
    bonus_percent = 10
else:
    print(f"Unknown grade {grade}")
    bonus_percent = 0
# Check if the salary is less than $10,000
if salary < 10000:
    bonus_percent += 2
# Calculate the bonus amount
bonus_amount = salary * bonus_percent / 100
# Print the final salary
final_salary = salary + bonus_amount
print(f"The employee will get a bonus of ${bonus_amount:.2f} and a final salary of ${final_salary:.2f}.")