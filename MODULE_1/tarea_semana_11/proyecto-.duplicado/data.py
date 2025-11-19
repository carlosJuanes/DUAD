
from actions import Student
import csv
import os


def import_student_file(file_path):
    imported_students = []
    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["Spanish Grade"] = float(row["Spanish Grade"])
                row["English Grade"] = float(row["English Grade"])
                row["Social Studies Grade"] = float(row["Social Studies Grade"])
                row["Science Grade"] = float(row["Science Grade"])
                row["Average"] = float(row["Average"])
                new_student=Student(row["Full name"], row["Section"], row["Spanish Grade"], row["English Grade"], row["Social Studies Grade"], row["Science Grade"], row["Average"])
                imported_students.append(new_student)
            return imported_students
    except Exception as error:
        print(f"An error occurred while importing {file_path}, the error is {error}")
        return []



def export_student_file(file_path, data, header):
    student_as_dicts=[]
    for student in data:
        student_dict={
            "Full name": student.full_name,
            "Section": student.section,
            "Spanish Grade": student.spanish_grade,
            "English Grade": student.english_grade,
            "Social Studies Grade": student.social_studies_grade,
            "Science Grade": student.science_grade,
            "Average": student.average,
        }
        student_as_dicts.append(student_dict)

    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(student_as_dicts)
