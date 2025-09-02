"""1. Refrescando la lectura de archivos"""
#1- Crea un archivo llamado frutas.txt (puedes hacerlo manualmente usando un editor de texto como el Bloc de Notas en Windows, 
# TextEdit en Mac, o cualquier editor de código) y pon tres frutas, una en cada línea. Por ejemplo:

# def lector_de_archivos(path):
#     with open(path) as file:
#         print(file.read())

# lector_de_archivos("frutas.txt")


"""2. Refrescando la escritura en archivos"""
# Escribe un programa Python que pida al usuario su nombre y luego lo guarde en un nuevo archivo llamado mi_nombre.txt. 
# Asegúrate de que, si ejecutas el programa varias veces, cada vez sobrescriba el nombre anterior 
# (es decir, el archivo solo debe contener el último nombre ingresado).

# def escritura_archivos(path):
#     name=input("por favor ingrese su nombre")
#     with open(path, "w") as file:
#         file.write(name)
# escritura_archivos("nombres.tx")

"""3. Refrescando la adición a archivos (modo append)"""
# Modifica tu programa Python anterior (archivos semana 8.py) para que, en lugar de sobrescribir el archivo mi_nombre.txt 
# cada vez que se ejecuta, añada el nuevo nombre del usuario al final del archivo sin borrar lo que ya estaba.

# def escritura_archivos(path):
#     name=input("porfavor ingrese su nombre= ")
#     with open(path, "a") as file:
#         file.write(name+"\n")
# escritura_archivos("nombres.txt")


"""4. Refrescando la Manipulación de Cadenas (quitar saltos de línea y mayúsculas)"""
# Pide al usuario una frase. Luego, tu programa debe hacer dos cosas y mostrarlas por consola:
# Mostrar esa frase en mayúsculas.
# Mostrar la frase sin ningún espacio al principio o al final, y sin ningún salto de línea oculto
#  que el usuario pueda haber ingresado accidentalmente.


# def convertir_string():
#     frase=input("ingrese una frase celebre= ")
#     frase_mayuscula=frase.upper()
#     print(f"frase mayuscula= {frase_mayuscula}")
#     frase_limpia=frase.strip()
#     print(f"frase sin espacios= {frase_limpia}")

# convertir_string()


"""Contar Palabras con split()"""
# Pide al usuario que ingrese una oración. Luego, cuenta cuántas palabras tiene esa oración y muestra el resultado por consola.

# def contar_palabras():
#     oracion=input("ingrese una oracion")
#     oracion_lista=oracion.split()
#     tamaño=len(oracion_lista)
#     print(tamaño)

# contar_palabras()


# libros=[["Romeo y Julieta", "William Shakespeare", 1597 ],
# ["El Decamerón", "Giovanni Boccaccio", 1353],
# ["Cien años de soledad", "Gabriel García Márquez", 1967],
# ["Don Quijote de la Mancha", "Miguel de Cervantes", 1605],
# ["Hamlet", "William Shakespeare", 1600],
# ["El Príncipe", "Nicolás Maquiavelo", 1532 ]]

# claves=["titulo", "autor", "anio_de_publicacion"]

# import csv

# def guardar_libros_csv(file_path, data, headers):
#     with open(file_path, "w", encoding="utf-8", newline='') as file:
#         writer=csv.writer(file)
#         writer.writerow(headers)
#         writer.writerows(data)

# guardar_libros_csv(libros.csv, libros, claves)


# import csv
# def leer_estudiantes_csv(file_path):
#     with open(file_path, 'r', newline='') as file:
#         reader=csv.reader(file)
#         for row in reader:
#             print(row)

# leer_estudiantes_csv("estudiantes.csv")


# import csv
# frutas_data = [
#     {'nombre': 'Manzana',
#     'color': 'Rojo',
#     'sabor': 'Dulce'
#     },
#     {'nombre': 'Limón',
#     'color': 'Verde',
#         'sabor': 'Ácido'
#         },
#     {'nombre': 'Banana', 
#     'color': 'Amarillo',
#     'sabor': 'Dulce'}
# ]

# encabezado=(
#     'nombre', 
#     'color',
#     'sabor'
# )

# def guardar_frutas_dict_csv(file_path, data, headers,):
#     with open(file_path, 'w', encoding="utf-8", newline="") as file:
#         writer=csv.DictWriter(file, fieldnames=headers)
#         writer.writeheader()
#         writer.writerows(data)

# guardar_frutas_dict_csv('frutas.csv', frutas_data, encabezado)

# import csv
# def buscar_por_categoria(file_path, categoria_buscada):
#     with open(file_path, 'r', newline="") as file:
#         reader=csv.DictReader(file)
#         for row in reader:
#             if row["Categoria"]==categoria_buscada:
#                 print(f"producto: {row["Producto"]}, precio:{row["Precio"]}")


# print("--- Productos Electrónicos ---")
# buscar_por_categoria('inventario.csv', 'Electronicos')
# print("\n--- Productos de Ropa ---")
# buscar_por_categoria('inventario.csv', 'Ropa')



# import csv

# def buscar_por_categoria(file_path, categoria_buscada):
#     with open(file_path, 'r', newline="") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             # Asegúrate de que 'Categoria' coincida con el encabezado de tu CSV
#             if row["Categoria"] == categoria_buscada:
#                 # Asegúrate de que 'Producto' y 'Precio' coincidan con los encabezados
#                 print(f"Producto: {row['Producto']}, Precio: {row['Precio']}")


# print("--- Productos Electrónicos ---")
# buscar_por_categoria('inventario.csv', 'Electronicos')

# print("\n--- Productos de Ropa ---")
# buscar_por_categoria('inventario.csv', 'Ropa')

# -----------------------------------------------------------------------------------

# import json

# # Abro el archivo 'libros.json' en modo lectura
# with open('libros.json.txt', 'r') as archivo:
#     # Leo el contenido y lo convierto en una lista de diccionarios de Python
#     libros = json.load(archivo)

# print(libros)
# print(f"El título del primer libro es: {libros[0]['titulo']}")



# --------------------------------------------------------------------------------------
# import json

# # Paso 1: Datos de Python
# # Tenemos una lista de diccionarios, que es la estructura de datos que usaremos.
# productos_py = [
#     {
#         'id': 1,
#         'nombre': 'Laptop',
#         'precio': 1200.50,
#         'en_stock': True
#     },
#     {
#         'id': 2,
#         'nombre': 'Teclado mecánico',
#         'precio': 95.00,
#         'en_stock': False
#     }
# ]

# print("--- Paso 1: Datos de Python ---")
# print(f"Tipo de datos original: {type(productos_py)}")
# print(f"Datos originales: {productos_py}")
# print("-" * 30)

# # Paso 2: Convertir de Python a un string JSON usando json.dumps()
# # Aquí, los datos de Python se "serializan" en un string.
# productos_json_string = json.dumps(productos_py, indent=4)

# print("--- Paso 2: Datos en formato JSON (como string) ---")
# print(f"Tipo del string JSON: {type(productos_json_string)}")
# print(f"String JSON:\n{productos_json_string}")
# print("-" * 30)

# # Paso 3: Convertir del string JSON de vuelta a Python usando json.loads()
# # Los datos se "deserializan" y se convierten de nuevo en una lista de diccionarios.
# productos_py_recuperados = json.loads(productos_json_string)

# print("--- Paso 3: Datos de Python recuperados ---")
# print(f"Tipo de datos recuperados: {type(productos_py_recuperados)}")
# print(f"Datos recuperados: {productos_py_recuperados}")
# print(f"Accediendo a un dato recuperado: {productos_py_recuperados[0]['nombre']}")


# ------------------------------------------------------------------------------------------------

import json

def cargar_pokemones(file_path):
    with open(file_path, "r") as file:
        archivo_py=json.load(file)
        return archivo_py


def crear_nuevo_pokemon():
    nombre=input("porfavor ingrese el nombre del nuevo pokemon: ")
    nombre_dict={"english":nombre}
    type_ingresado=input("porfavor ingrese el tipo de pokemon: ")
    type_list=[type_ingresado]
    print("porfavor ingrese la informacion de la base")
    base_hp=int(input("porfavor ingrese el hp: "))
    base_attack=int(input("porfavor ingrese el attack: "))
    base_defense=int(input("porfavor ingrese la defensa: "))
    base_sp_attack=int(input("porfavor ingrese el sp attack: "))
    base_sp_defense=int(input("porfavor ingrese el sp defense: "))
    base_speed=int(input("porfavor ingrese el speed: "))
    base_dict={
      "HP": base_hp,
      "Attack": base_attack,
      "Defense": base_defense,
      "Sp. Attack": base_sp_attack,
      "Sp. Defense": base_sp_defense,
      "Speed": base_speed
      }
    nuevo_pokemon_completo={
        "name":nombre_dict,
        "type":type_list,
        "base":base_dict
    }
    return nuevo_pokemon_completo

pokemones_existentes=cargar_pokemones("pokemones.json.txt")
nuevo_pokemon=crear_nuevo_pokemon()
pokemones_existentes.append(nuevo_pokemon)


with open("pokemones.json.txt", "w") as file:
    json.dump(pokemones_existentes, file, indent=4)

print(" el nuevo pokemon ha sido agregado exitosamente y el archivo a sido guardado")


# # ----------------------------------------------------------------------------------------
# 1. Cree un programa que abra un archivo `.json` con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# - Lea el archivo `JSON` de Pokémon
# - Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)
import json

def cargar_pokemones(file_path):
    with open(file_path, "r") as file:
        archivo_py=json.load(file)
        return archivo_py
    
    
pokemones_existentes=cargar_pokemones("pokemones.json.txt")


for pokemon in pokemones_existentes:
    print(f'Name= {pokemon["name"]["english"]}')
    print(f'Type= {pokemon["type"]}')
    print("Bases")
    print(f'HP= {pokemon["base"]["HP"]}')
    print(f'Attack= {pokemon["base"]["Attack"]}')
    print(f'Defense= {pokemon["base"]["Defense"]}')
    print(f'Sp. Attack= {pokemon["base"]["Sp. Attack"]}')
    print(f'Sp. Defense= {pokemon["base"]["Sp. Defense"]}')
    print(f' Speed= {pokemon["base"]["Speed"]}')

buscar_type=input("Ingrese el tipo de pokemon desea buscar(agua,electrico,fuego,etc):")
type_minuscula=buscar_type.lower()
pokemones_encontrados = []
for pokemon in pokemones_existentes:
    tipos_del_pokemon = [tipo.lower() for tipo in pokemon["type"]]
    if type_minuscula in tipos_del_pokemon:
        pokemones_encontrados.append(pokemon["name"]["english"])
if pokemones_encontrados:
    print("Los pokemos que existen de ese tipo son: ")
    for nombre in pokemones_encontrados:
        print(nombre)
else:
    print(f"No se encontró ningún Pokémon del tipo '{buscar_type}'.")


import json

def cargar_pokemones(file_path):
    with open(file_path, "r") as file:
        archivo_py=json.load(file)
        return archivo_py
    
    
pokemones_existentes=cargar_pokemones("pokemones.json.txt")

for pokemon in pokemones_existentes:
    print(f' nombre: {pokemon["name"]["english"]}')
    print(f'Ataque: {pokemon["base"]["Attack"]}')
    print(f' Defensa: {pokemon["base"]["Defense"]}')
    print(f' Velocidad: {pokemon["base"]["Speed"]}')



    # ---------------------------------------------------------------------------------------------
import json

def cargar_pokemones(file_path):
    with open(file_path, "r") as file:
        archivo_py=json.load(file)
        return archivo_py
    
    
pokemones_existentes=cargar_pokemones("pokemones.json.txt")


nivel_pokemons={}
def calcular_promedio(num_list):
    suma_total=sum(num_list)
    elementos=len(num_list)
    promedio=suma_total/elementos
    return promedio

for pokemon in pokemones_existentes:
    pokemon_base=pokemon["base"]
    nivel_de_pokemon=calcular_promedio(pokemon_base.values())
    for tipo in pokemon["type"]:
        if tipo in nivel_pokemons:
            nivel_pokemons[tipo].append(nivel_de_pokemon)
        else:
            nivel_pokemons[tipo]=[nivel_de_pokemon]

for clave, valor in nivel_pokemons.items():
    promedio_de_clave=calcular_promedio(valor)
    print(f"tipo {clave} promedio de nivel: {promedio_de_clave:.2f}")

    # -----------------------------------------------------
    import json

def cargar_pokemones(file_path):
    with open(file_path, "r") as file:
        archivo_py = json.load(file)
        return archivo_py

def calcular_promedio(num_list):
    suma_total = sum(num_list)
    elementos = len(num_list)
    promedio = suma_total / elementos
    return promedio

# Cargar los datos
pokemones_existentes = cargar_pokemones("pokemones.json.txt")

# Diccionario para agrupar los niveles
nivel_pokemons = {}

# Agrupar los niveles por tipo en el diccionario
for pokemon in pokemones_existentes:
    nivel_de_pokemon = calcular_promedio(pokemon["base"].values())
    for tipo in pokemon["type"]:
        if tipo in nivel_pokemons:
            nivel_pokemons[tipo].append(nivel_de_pokemon)
        else:
            nivel_pokemons[tipo] = [nivel_de_pokemon]

# Calcular y mostrar los promedios finales
for clave, valor in nivel_pokemons.items():
    promedio_de_clave = calcular_promedio(valor)
    print(f"Tipo {clave} promedio de nivel: {promedio_de_clave:.2f}")