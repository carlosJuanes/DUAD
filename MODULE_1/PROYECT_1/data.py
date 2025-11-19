import csv
import os


def exportar_archivo_de_estudiantes(file_path, data, header):
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer=csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)

def importar_archivo_de_estudiantes(file_path):
    estudiantes_importados=[]
    try:
        with open(file_path, "r",newline="") as file:
            reader=csv.DictReader(file)
            for row in reader:
                row["Nota de Español"]=float(row["Nota de Español"])
                row["Nota de Ingles"]=float(row["Nota de Ingles"])
                row["Nota de Sociales"]=float(row["Nota de Sociales"])
                row["Nota de Ciencias"]=float(row["Nota de Ciencias"])
                row["Promedio"]=float(row["Promedio"])
                estudiantes_importados.append(row)
            return estudiantes_importados
    except Exception as error:
        print(f"Ocurrion un erro al importar {file_path}, el error es {error}")
        return []