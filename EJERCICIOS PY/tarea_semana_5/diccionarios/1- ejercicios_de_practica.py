


empresa = {
    "nombre": "Tech Solutions Inc.",
    "rubro": "Tecnología y Software",
    "departamentos": [
        {
            "funcion": "Desarrollo de software",
            "numero_personal": 75,
            "nombre_presidente": "Dr. Elena García"
        },
        {
            "funcion": "Marketing digital",
            "numero_personal": 30,
            "nombre_presidente": "Lic. Pablo Ruiz"
        },
        {
            "funcion": "Recursos humanos",
            "numero_personal": 15,
            "nombre_presidente": "Mtra. Sofía López"
        }
    ]
}

print(empresa)



# print("--- Usando .keys() ---")
# claves_empresa = empresa.keys()
# print(f"Las claves del diccionario 'empresa' son: {claves_empresa}")

# # Puedes iterar sobre ellas:
# print("\nIterando sobre las claves:")
# for clave in empresa.keys():
#     print(clave)


# print("\n--- Usando .values() ---")
# valores_empresa = empresa.values()
# print(f"Los valores del diccionario 'empresa' son: {valores_empresa}")

# # Puedes iterar sobre ellos:
# print("\nIterando sobre los valores:")
# for valor in empresa.values():
#     print(valor)


# print("\n--- Usando .items() ---")
# items_empresa = empresa.items()
# print(f"Los items del diccionario 'empresa' son: {items_empresa}")

# # Puedes iterar sobre ellos, desempaquetando en dos variables:
# print("\nIterando sobre los items (clave y valor):")
# for clave, valor in empresa.items():
#     print(f"Clave: {clave}, Valor: {valor}")


# print("\n--- Agregando/Actualizando Datos ---")
# print(f"Diccionario antes de agregar/actualizar: {empresa}")

# # Agregamos una nueva clave 'fundacion'
# empresa["fundacion"] = 2005
# print(f"Diccionario después de agregar 'fundacion': {empresa}")

# # Agregamos una nueva clave 'ubicacion'
# empresa["ubicacion"] = "Silicon Valley"
# print(f"Diccionario después de agregar 'ubicacion': {empresa}")

# # Actualizamos el 'rubro' existente
# empresa["rubro"] = "Tecnología, Software y Consultoría"
# print(f"Diccionario después de actualizar 'rubro': {empresa}")



# print("\n--- Eliminando Datos ---")
# print(f"Diccionario antes de eliminar: {empresa}")

# # Usando del para eliminar 'ubicacion'
# del empresa["ubicacion"]
# print(f"Diccionario después de eliminar 'ubicacion' con del: {empresa}")

# # Usando pop() para eliminar 'fundacion' y obtener su valor
# valor_fundacion = empresa.pop("fundacion")
# print(f"Diccionario después de eliminar 'fundacion' con pop(): {empresa}")
# print(f"El valor de 'fundacion' que se eliminó fue: {valor_fundacion}")

# # Intentar eliminar una clave que no existe con pop() y un valor por defecto
# valor_inexistente = empresa.pop("ceo", "No hay CEO registrado")
# print(f"Intentando eliminar 'ceo': {valor_inexistente}")
# print(f"Diccionario después de intentar eliminar 'ceo': {empresa}")

# Para eliminar todos los elementos: .clear()
# empresa.clear()
# print(f"Diccionario después de clear(): {empresa}")