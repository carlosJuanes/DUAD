import csv
import os


def export_student_file(file_path, data, header):
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)


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
                imported_students.append(row)
            return imported_students
    except Exception as error:
        print(f"An error occurred while importing {file_path}, the error is {error}")
        return []
