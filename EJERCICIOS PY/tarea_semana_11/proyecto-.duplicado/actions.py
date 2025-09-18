class Student:
    def __init__(self, full_name, section, spanish_grade, english_grade, social_studies_grade, science_grade, average):
        self.full_name=full_name
        self.section=section
        self.spanish_grade=spanish_grade
        self.english_grade=english_grade
        self.social_studies_grade=social_studies_grade
        self.science_grade=science_grade
        self.average=average


def validate_name():
    while True:
        name_entered = input("Please enter the full name: ")
        clean_name = name_entered.strip()
        if not clean_name:
            print("The name cannot be empty")
            continue
        valid_name = True
        for character in clean_name:
            if not character.isalpha() and character != " ":
                valid_name = False
                break
        if valid_name:
            return clean_name
        else:
            print("The name must only contain letters and spaces")


def validate_section():
    while True:
        section = input("Please enter the student's section: ")
        clean_section = section.strip()
        if not clean_section:
            print("The section cannot be empty")
            continue
        if len(clean_section) == 3:
            if clean_section[0:2].isdigit() and clean_section[2].isalpha():
                return clean_section.upper()
            else:
                print("Invalid section format. The format must be 1A, 2B, 10A, 11B, etc.")
        elif len(clean_section) == 2:
            if clean_section[0].isdigit() and clean_section[1].isalpha():
                return clean_section.upper()
            else:
                print("Invalid section format. The format must be 1A, 2B, 10A, 11B, etc.")
        else:
            print("Invalid section format. The format must be 1A, 2B, 10A, 11B, etc.")


def student_exists(students, name, section):
    for student in students:
        if student.full_name == name and student.section == section:
            return True
    return False

def enter_student(students):
    grades_list = []
    name = validate_name().upper()
    section = validate_section().upper()
    if student_exists(students, name, section):
        print("The student you are trying to enter already exists in our database")
        return
    subjects = ["Spanish Grade", "English Grade", "Social Studies Grade", "Science Grade"]
    for subject in subjects:
        while True:
            try:
                grade = int(input(f"Please enter the grade for {subject}="))
                if 0 <= grade <= 100:
                    grades_list.append(grade)
                    break
                else:
                    print("Please enter a valid grade from 0-100")
            except ValueError:
                print("Please enter a valid number")
    size = len(grades_list)
    total = sum(grades_list)
    average = total / size
    return Student(name, section, grades_list[0], grades_list[1], grades_list[2], grades_list[3], average)

def show_students(students):
    if students:
        print("---------------------------------")
        print("STUDENT DATABASE")
        print("---------------------------------")
        for i, student in enumerate(students, 1):
            print(f"\nStudent number {i}")
            print(f"Full name: {student.full_name}")
            print(f"Section: {student.section}")
            print(f"Spanish grade: {student.spanish_grade}")
            print(f"English grade: {student.english_grade}")
            print(f"Social studies grade: {student.social_studies_grade}")
            print(f"Science grade: {student.science_grade}")
            print(f"Average: {student.average}")
    else:
        print("There is no information in our database yet, please enter a student first")



def show_the_best_averages(students):
    if students:
        students.sort(key=lambda student: student.average, reverse=True)
        top_3_students = students[:3]
        print("---TOP THREE HIGHEST AVERAGES---")
        for i, student in enumerate(top_3_students, 1):
            print(f"Rank number {i}")
            print(f"Full name: {student.full_name}")
            print(f"Section: {student.section}")
            print(f"Spanish grade: {student.spanish_grade}")
            print(f"English grade: {student.english_grade}")
            print(f"Social studies grade: {student.social_studies_grade}")
            print(f"Science grade: {student.science_grade}")
            print(f"Average: {student.average}")
            print()
    else:
        print("There is no information in our database yet, please enter a student first")



def show_the_total_average(students):
    if students:
        averages = [student.average for student in students]
        total_average = sum(averages) / len(averages)
        print(f"The total average grade of the students is: {total_average}")
    else:
        print("There is no information in our database yet, please enter a student first")



def delete_student(students):
    student_to_delete = None
    name_to_delete = input("Please enter the full name of the student to delete: ")
    section_to_delete = input("Please enter the student's section to delete: ")
    uppercase_student_to_delete = name_to_delete.upper()
    uppercase_section_to_delete = section_to_delete.upper()
    for i, student in enumerate(students):
        if student.full_name == uppercase_student_to_delete and student.section == uppercase_section_to_delete:
            print(f"Student {uppercase_student_to_delete} from section {uppercase_section_to_delete} has been found")
            index_to_delete = i
            student_to_delete = student
            break
    if student_to_delete is None:
        print("The student was not found in our database.")
    else:
        while True:
            try:
                confirmation = int(input("Are you sure you want to delete it? Press 1 for yes, or press 2 for no"))
                if confirmation == 1:
                    students.pop(index_to_delete)
                    print("The student has been successfully deleted from the database!!!")
                    break
                elif confirmation == 2:
                    print("Action cancelled")
                    break
                else:
                    print("Please enter a valid number from 1-2")
            except ValueError:
                print("Please enter a valid number")


def show_failing_students(students):
    print("\n--- Failing Students ---")
    failing_students_found = False
    for student in students:
        failing_grades = {}
        if student.spanish_grade < 60:
            failing_grades["Spanish Grade"] = student.spanish_grade
        if student.english_grade < 60:
            failing_grades["English Grade"] = student.english_grade
        if student.social_studies_grade < 60:
            failing_grades["Social Studies Grade"] = student.social_studies_grade
        if student.science_grade < 60:
            failing_grades["Science Grade"] = student.science_grade
        if failing_grades:
            print("\n------------------------------")
            print(f"Name: {student.full_name}")
            print(f"Section: {student.section}")
            print("Failing Subjects")
            for key, value in failing_grades.items():
                print(f"{key}: {value}")
                failing_students_found = True
    if not failing_students_found:
        print("No failing students were found")
