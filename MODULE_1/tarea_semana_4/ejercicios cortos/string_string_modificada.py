print("--- Iterando sobre una Lista ---")
frutas = ["manzana", "banana", "cereza"]

for fruta_actual in frutas:
    print(f"Me gusta comer {fruta_actual}")

print("\n") # Esto es solo para dejar un espacio en la salida

print("--- Iterando sobre una Cadena de Texto ---")
palabra = "Python"

for letra in palabra:
    print(f"Letra: {letra}")

print("\n")


# --- Ejemplo de Iteración con una Oración Completa ---
print("--- Iterando sobre una Oración Completa ---")
oracion = "¡Hola, estoy aprendiendo Python!"

for caracter in oracion:
    print(f"Carácter: '{caracter}'") # Uso comillas simples para que veas los espacios también

print("\n")

# --- Otro ejemplo: un número como string ---
print("--- Iterando sobre un número como String ---")
numero_como_texto = "12345"

for digito in numero_como_texto:
    print(f"Dígito: {digito}")

print("\n")



print("--- Iterando sobre un Rango ---")
# Esto imprimirá números del 0 al 4 (el 5 no se incluye)
for numero in range(5):
    print(f"Número actual: {numero}")

print("\n")




print("--- Iterando sobre un Diccionario (claves) ---")
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}

for clave in persona: # Por defecto, itera sobre las claves
    print(f"Clave: {clave}")

print("\n")

# Si quieres los valores del diccionario, puedes hacer esto:
print("--- Iterando sobre un Diccionario (valores) ---")
for valor in persona.values():
    print(f"Valor: {valor}")

print("\n")

# Y si quieres ambos (clave y valor), puedes hacer esto:
print("--- Iterando sobre un Diccionario (clave y valor) ---")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")



    # --- Ejemplo: Iteración por Índice con una Lista ---
print("--- Iteración por Índice con una Lista ---")
frutas = ["manzana", "banana", "cereza"]

# 1. Obtenemos la longitud de la lista
cantidad_de_frutas = len(frutas) # Esto nos da 3

# 2. Usamos range para generar los índices (0, 1, 2)
# range(cantidad_de_frutas) es lo mismo que range(3), que nos da 0, 1, 2
for indice in range(cantidad_de_frutas):
    # 3. Usamos el índice para acceder al elemento en esa posición
    fruta_actual = frutas[indice]
    print(f"La fruta en el índice {indice} es: {fruta_actual}")

print("\n")