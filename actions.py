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
        if student["Full name"] == name and student["Section"] == section:
            return True
    return False


def enter_student(students):
    student_entered = {}
    name = validate_name().upper()
    section = validate_section().upper()
    if student_exists(students, name, section):
        print("The student you are trying to enter already exists in our database")
        return
    student_entered["Full name"] = name
    student_entered["Section"] = section
    subjects = ["Spanish Grade", "English Grade", "Social Studies Grade", "Science Grade"]
    for subject in subjects:
        while True:
            try:
                grade = int(input(f"Please enter the grade for {subject}="))
                if 0 <= grade <= 100:
                    student_entered[subject] = grade
                    break
                else:
                    print("Please enter a valid grade from 0-100")
            except ValueError:
                print("Please enter a valid number")
    grades = [student_entered["Spanish Grade"], student_entered["English Grade"], student_entered["Social Studies Grade"], student_entered["Science Grade"]]
    size = len(grades)
    total = sum(grades)
    average = total / size
    student_entered["Average"] = average
    return student_entered


def show_students(students):
    if students:
        print("---------------------------------")
        print("STUDENT DATABASE")
        print("---------------------------------")
        for i, student in enumerate(students, 1):
            print(f"\nStudent number {i}")
            for key, value in student.items():
                print(f"{key}:{value}")
    else:
        print("There is no information in our database yet, please enter a student first")


def show_the_best_averages(students):
    if students:
        students.sort(key=lambda student: student["Average"], reverse=True)
        top_3_students = students[:3]
        print("---TOP THREE HIGHEST AVERAGES---")
        for i, student in enumerate(top_3_students, 1):
            print(f"Rank number {i}")
            for key, value in student.items():
                print(f"{key}: {value}")
            print()
    else:
        print("There is no information in our database yet, please enter a student first")


def show_the_total_average(students):
    if students:
        averages = [student["Average"] for student in students]
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
        if student["Full name"] == uppercase_student_to_delete and student["Section"] == uppercase_section_to_delete:
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
        if student["Spanish Grade"] < 60:
            failing_grades["Spanish Grade"] = student["Spanish Grade"]
        if student["English Grade"] < 60:
            failing_grades["English Grade"] = student["English Grade"]
        if student["Social Studies Grade"] < 60:
            failing_grades["Social Studies Grade"] = student["Social Studies Grade"]
        if student["Science Grade"] < 60:
            failing_grades["Science Grade"] = student["Science Grade"]
        if failing_grades:
            print("\n------------------------------")
            print(f"Name: {student['Full name']}")
            print(f"Section: {student['Section']}")
            print("Failing Subjects")
            for key, value in failing_grades.items():
                print(f"{key}: {value}")
                failing_students_found = True
    if not failing_students_found:
        print("No failing students were found")

        