libros=[["Romeo y Julieta", "William Shakespeare", 1597 ],
["El Decamerón", "Giovanni Boccaccio", 1353],
["Cien años de soledad", "Gabriel García Márquez", 1967],
["Don Quijote de la Mancha", "Miguel de Cervantes", 1605],
["Hamlet", "William Shakespeare", 1600],
["El Príncipe", "Nicolás Maquiavelo", 1532 ]]

claves=["titulo", "autor", "anio_de_publicacion"]

import csv

def guardar_libros_csv(file_path, data, headers):
    with open(file_path, "w", encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

guardar_libros_csv("libros.csv", libros, claves)