

import csv
import data
import actions


def show_menu():
    print("Welcome to the student database")
    print(f"What would you like to do?:\n"
          f"1- Enter information for n number of students, one by one.\n"
          f"2- View the information of all entered students.\n"
          f"3- View the top 3 students with the best average grade.\n"
          f"4- View the average grade among all students.\n"
          f"5- Export all current data to a CSV file.\n"
          f"6- Import data from a previously exported CSV file.\n"
          f"7- Delete a student by Name and Section\n"
          f"8- Show Failing Students\n"
          f"9- Exit.")


def select_option():
    while True:
        try:
            option = int(input("Please enter an option= "))
            if 1 <= option <= 9:
                return option
            else:
                print("Error, please select a valid option from 1-9")
        except ValueError:
            print("Error! This is not a valid option")


def run():
    students = []
    headers = ["Full name", "Section", "Spanish Grade", "English Grade", "Social Studies Grade", "Science Grade", "Average"]
    while True:
        print("-------------------------------------------")
        print("-------------- STUDENT DATABASE -----------")
        print("-------------------------------------------")
        show_menu()
        selected_option = select_option()
        if selected_option == 1:
            while True:
                try:
                    quantity = int(input("How many students do you want to enter?= "))
                    for n in range(quantity):
                        print(f"Student N{n+1}:")
                        new_student = actions.enter_student(students)
                        students.append(new_student)
                    break
                except ValueError:
                    print("Please enter a valid number")
        elif selected_option == 2:
            actions.show_students(students)
        elif selected_option == 3:
            actions.show_the_best_averages(students)
        elif selected_option == 4:
            actions.show_the_total_average(students)
        elif selected_option == 5:
            if students:
                data.export_student_file("student_data.csv", students, headers)
                print("Student data has been successfully exported to a CSV file")
            else:
                print("There is no information in our database yet, please enter a student first")
        elif selected_option == 6:
            imported_students = data.import_student_file("student_data.csv")
            if imported_students:
                students = imported_students
                print("The file has been successfully imported")
                print("The imported student list is:")
                for i, student in enumerate(students, 1):
                    print(f"Student number {i}")
                    print(f"Full name= {student.full_name}")
                    print(f"Section= {student.section}")
                    print(f"Spanish Grade= {student.spanish_grade}")
                    print(f"English Grade= {student.english_grade}")
                    print(f"Social Studies Grade= {student.social_studies_grade}")
                    print(f"Science Grade= {student.science_grade}")
                    print(f"Average= {student.average}")
            else:
                print("There is no file to import")
        elif selected_option == 7:
            actions.delete_student(students)
        elif selected_option == 8:
            actions.show_failing_students(students)
        elif selected_option == 9:
            print("Exiting...")
            print("Goodbye!!!")
            break


        