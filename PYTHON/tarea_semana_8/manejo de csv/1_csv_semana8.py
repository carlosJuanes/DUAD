# # Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.

# import csv

# header=["nombre", "genero", "desarrollador", "clasificacion"]
# def ingresar_videojuegos():
#     videojuegos=[]
#     while True:
#         videojuegos_ingresados=input("desea ingresar videojuegos a la base de datos?")
#         videojuegos_minuscula=videojuegos_ingresados.lower()
#         if videojuegos_minuscula=="si":
#             nombre=input("ingrese el nombre del videojuego= ")
#             genero=input("ingrese el genero del videojuego= ")
#             desarrollador=input("ingrese el desarrollador del videojuego= ")
#             clasificacion=input("ingrese la clasificacion del videojuego= ")
#             videojuego_actual={
#                 "nombre":nombre,
#                 "genero":genero,
#                 "desarrollador":desarrollador,
#                 "clasificacion":clasificacion
#             }
#             videojuegos.append(videojuego_actual)
#         elif videojuegos_minuscula=="no":
#             break
#         else:
#             print("respuesta no valida, Porfavor ingrese si o no")
#     return videojuegos


# def guardar_videojuegos(file_path, data, header):
#     with open(file_path, "w",encoding="utf-8", newline="") as file:
#         writer=csv.DictWriter(file,fieldnames=header)
#         writer.writeheader()
#         writer.writerows(data)


# mis_juegos=ingresar_videojuegos()
# guardar_videojuegos("videojuegos.csv",mis_juegos,header)



# def lector_de_archivos(file_path):
#     juegos_guardados=[]
#     with open(file_path, "r", newline="") as file:
#         reader=csv.DictReader(file)
#         for row in reader:
#             juegos_guardados.append(row)
#     return juegos_guardados


# lector_de_archivos("videojuegos.csv")

# def mostrar_videojuegos(lista_de_juegos):
#     print("\n--- Videojuegos Registrados ---")
#     if not lista_de_juegos:
#         print("no hay juegos registrados aun")
#         return
    
#     for index, juego in enumerate(lista_de_juegos):
#         numero_de_juego=index+1
#         print(f" numero de juego {numero_de_juego}")
#         print(f'{juego["nombre"], juego["genero"], juego["desarrollador"], juego["clasificacion"]} ')


# ------------------------------------------------------------------------------------------------------

# Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.

# import csv

# def pedir_datos():
#     nombre_del_juego=input("porfavor ingrese el nombre del videojuego")
#     genero_del_juego=input("porfavor ingrese el genero del videojuego")
#     desarrollador_del_juego=input("porfavor ingrese el desarrollador del videojuego")
#     clasificacion_del_juego=input("porfavor ingrese la clasificacion del videojuego")
#     juego_actual={
#         "nombre":nombre_del_juego,
#         "genero":genero_del_juego,
#         "desarrollador":desarrollador_del_juego,
#         "clasificacion":clasificacion_del_juego
#     }
#     return juego_actual


# def recopilar_videojuegos():
#     datos_de_videojuegos=[]
#     while True:
#         ingresar_datos=input("desea ingresar videojuegos a la base de datos? ")
#         datos_minusculas=ingresar_datos.lower()
#         if datos_minusculas=="si":
#             nuevo_videojuego=pedir_datos()
#             datos_de_videojuegos.append(nuevo_videojuego)
#         elif datos_minusculas=="no":
#             break
#         else:
#             print("no es una entrada valida, porfavor ingrese si o no")
#     return datos_de_videojuegos

# claves=["nombre", "genero", "desarrollador", "clasificacion"]
# def guardar_en_csv(file_path, data_list, header):
#     with open(file_path, "w",  encoding='utf-8') as file:
#         writer=csv.DictWriter(file, header, delimiter="\t")
#         writer.writeheader()
#         writer.writerows(data_list)

# guardar_en_csv("videojuegos.csv", recopilar_videojuegos(), claves)


# -------------------------------------------------------------------------------------------------------------

# 3-. Cree un programa que abra un archivo `.csv` con la información de videojuegos (el que fue generado en el ejercicio 1) y:
# - Lea cada línea usando `csv.reader()`
# - Muestre el contenido en pantalla de forma legible, línea por línea
# import csv
# def lector_de_archivo(path):
#     with open(path, "r", newline='') as file:
#         reader=csv.reader(file)
#         encabezados=next(reader)
#         for row in reader:
#             # for index in range(len(encabezados)):
#             #     first=encabezados[index]
#             #     second=row[index]
#             #     print(f"{first}:{second} ")
#             # print()
#             for clave, valor in zip(encabezados, row):
#                 print(f"{clave}:{valor}")
#             print()

# lector_de_archivo("videojuegos.scv")

# ----------------------------------------------------------------------------------------------------------
# 4- Cree un programa que abra un archivo `.csv` con la información de videojuegos 
# ( en base al CSV que fue generado en el ejercicio 1) y:
# - Lea el archivo CSV de videojuegos
# - Pida al usuario una clasificación ESRB (por ejemplo: "T")
# - Muestre todos los videojuegos que tengan esa clasificación

# import csv

# def buscar_por_clasificacion_videojuegos(file_path):
#     with open(file_path, "r", newline="") as file:
#         reader=csv.DictReader(file)
#         clasificacion_buscada=input("ingrese la  clasificación ESRB que busca")
#         clasificacion_mayuscula=clasificacion_buscada.upper()
#         found_game=False
#         for row in reader:
#             if clasificacion_mayuscula==row["clasificacion"].upper():
#                 found_game=True
#                 for clave, valor in row.items():
#                     print(f"{clave}:{valor}")
#                 print()
#         if not found_game:
#             print(f"no se encontraron videojuegos con la clasificacion {clasificacion_buscada} ")

# buscar_por_clasificacion_videojuegos("videojuegos.csv")

# -------------------------------------------------------------------------------------------------------
# Cree un programa que abra un archivo .csv con la información de videojuegos 
# ( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo .csv con videojuegos 
# Cuente cuántos videojuegos hay de cada género
# Muestre el resultado de forma ordenada


# import csv 
# def contar_generos(file_path):
#     contador_de_videojuegos={}
#     with open(file_path, "r", newline="") as file:
#         lector=csv.DictReader(file)
#         for row in lector:
#             genero_actual=row["genero"]
#             if genero_actual in contador_de_videojuegos:
#                 contador_de_videojuegos[genero_actual]+=1
#             else:
#                 contador_de_videojuegos[genero_actual]=1
#     diccionario_ordenado=sorted(contador_de_videojuegos.keys())
#     print ("generos encontrados")
#     for genero in diccionario_ordenado:
#         conteo=contador_de_videojuegos[genero]
#         print(f"{genero}:{conteo}")

# contar_generos("videojuegos.csv")



# ---------------------------------------------------------------------------------------------------------

# 1. Cree un programa que abra un archivo `.csv` con la información de videojuegos
# ( en base al CSV que fue generado en el ejercicio 1) y:
# - Lea el archivo `.csv` con videojuegos
# - Pida al usuario ingresar el nombre de un **desarrollador** (ej. `"Ubisoft"`)
# - Muestre todos los videojuegos desarrollados por esa empresa en formato legible:

# import csv
# def desarrollador_de_videojuegos(file_path):
#     with open(file_path, "r", newline="") as file:
#         reader=csv.DictReader(file)
#         desarrollador_ingresado=input("porfavor ingrese el nombre del desarrollador")
#         desarrollador_minuscula=desarrollador_ingresado.lower()
#         found_game=False
#         for row in reader:
#             if row["desarrollador"].lower()==desarrollador_minuscula:
#                 found_game=True
#                 print(f"Videojuegos desarrollados por {desarrollador_minuscula}:")
#                 print(f"row["Nombre"], (clasificacion: row["clasificacion"], Genero: row["genero"])")
#         if not found_game:
#             print("no se encontro el desarrollador")









# import csv

# def desarrollador_de_videojuegos(file_path):
#     with open(file_path, "r", newline="") as file:
#         reader = csv.DictReader(file)
#         desarrollador_ingresado = input("Por favor, ingrese el nombre del desarrollador: ")
#         desarrollador_minuscula = desarrollador_ingresado.lower()
#         found_game = False

#         # Creamos una lista para guardar los videojuegos encontrados
#         juegos_encontrados = []

#         for row in reader:
#             if row["desarrollador"].lower() == desarrollador_minuscula:
#                 found_game = True
#                 # Guardamos cada juego que coincide en la lista
#                 juegos_encontrados.append(row)
        
#         if found_game:
#             # Imprimimos el encabezado UNA SOLA VEZ antes del bucle
#             print(f"Videojuegos desarrollados por {desarrollador_ingresado}:")
#             # Iteramos sobre los juegos que ya encontramos
#             for juego in juegos_encontrados:
#                 # Usamos una f-string corregida para el formato de salida
#                 print(f"- {juego['nombre']} (Clasificación: {juego['clasificacion']}, Género: {juego['genero']})")
#         else:
#             print(f"No se encontraron videojuegos del desarrollador {desarrollador_ingresado}.")

# # Ejemplo de cómo llamar a la función
# desarrollador_de_videojuegos("videojuegos.csv")


