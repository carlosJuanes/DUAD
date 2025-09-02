#5. Given n number of student grades, calculate:
    #How many approved grades there are (greater than 70).
    #How many failed grades there are (less than 70).
    #The average of all grades.
    #The average of the approved grades.
    #The average of the failed grades.

counter = 1
current_grade = 0
approved_grades_count = 0
failed_grades_count = 0
approved_grades_sum = 0  
failed_grades_sum = 0    
total_grades_sum = 0     

total_number_of_grades = int(input(f"Enter the total number of grades: "))

while counter <= total_number_of_grades:
    current_grade = int(input(f"Enter grade number {counter}: "))
    if current_grade < 70:
        failed_grades_sum += current_grade
        failed_grades_count += 1
    else:  
        approved_grades_sum += current_grade
        approved_grades_count += 1

    total_grades_sum += current_grade
    counter += 1

overall_average = total_grades_sum / total_number_of_grades


if approved_grades_count > 0:
    approved_grades_average = approved_grades_sum / approved_grades_count
else:
    approved_grades_average = 0  

if failed_grades_count > 0:
    failed_grades_average = failed_grades_sum / failed_grades_count
else:
    failed_grades_average = 0 

print(f"The student passed {approved_grades_count} exams.")
print(f"The student failed {failed_grades_count} exams.")
print(f"The average of approved grades is {approved_grades_average:.0f}%.")
print(f"The average of failed grades is {failed_grades_average:.0f}%.")
print(f"The overall average grade is {overall_average:.0f}%.")
