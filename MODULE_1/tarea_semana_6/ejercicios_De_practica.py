def print_hello_world():
	print("Hello World!")
	print("Mi primera funcion")


print_hello_world()
print_hello_world()



def print_sum_of_numbers(number_a, number_b=5):
	print(number_a + number_b)


print_sum_of_numbers(4)

def sum_three_numbers(number1, number2, number3):
	return number1 + number2 + number3


result = sum_three_numbers(600, 700, 800)
print(result)





def get_max_of_two_numbers(number1, number2):
  if number1 > number2:
    return number1

  return number2


print(get_max_of_two_numbers(3, 7))

print("          ")
print("          ")
print("          ")
print("          ")

def sum_three_numbers(number1, number2, number3):
	return number1 + number2 + number3


result = sum_three_numbers(600, 700, 800)
print(result)




print("      ")


# def declare_variable():
#   variable_inside_function_scope = 8
#   print(f'Inside function: {variable_inside_function_scope}')


# declare_variable()
# print(f'Out of function: {variable_inside_function_scope}')

print("      ") 
print("      ")
print("      ")
print("      ")
print("      ")

variable_outside_function_scope = 7

def print_variable():
  print(f'Inside function: {variable_outside_function_scope}')


print_variable()
print(f'Outside function: {variable_outside_function_scope}')


def saludar():
  """Esta función saluda e invoca a otra función para decir qué hace."""
  print("¡Hola! Soy la función 'saludar'.")
  describir_proposito() # Aquí es donde la primera función llama a la segunda

def describir_proposito():
  """Esta función explica el propósito de nuestro ejercicio."""
  print("Mi propósito es mostrar cómo una función puede llamar a otra.")

# Ahora, llamamos a la primera función para iniciar el proceso
saludar()


print("---------------------")


def mi_funcion():
  # Esta variable 'mensaje_local' está definida DENTRO de la función.
  # Su scope es LOCAL a 'mi_funcion'.
  mensaje_local = "¡Hola desde dentro de la función!"
  print(mensaje_local) # Aquí sí se puede acceder y usar

# Llamamos a la función para que se ejecute su contenido.
mi_funcion()

# Intentamos acceder a 'mensaje_local' desde AFUERA de la función.
# ¡Esto causará un error!
# print(mensaje_local) # Descomenta esta línea para ver el error NameError




# print("--------------")
# # Esta variable 'contador_global' es GLOBAL.
# # Su scope es GLOBAl, lo que significa que es accesible desde cualquier parte del código.
# contador_global = 10

# def incrementar_contador():
#   # Podemos acceder a 'contador_global' desde dentro de la función para LEER su valor.
#   print(f"Dentro de la función (antes de cambiar): {contador_global}")

#   # Si intentamos REASIGNAR 'contador_global' directamente,
#   # Python creará una NUEVA variable LOCAL con el mismo nombre,
#   # a menos que usemos la palabra clave 'global'.
#   # Por defecto, esta línea crearía una variable local 'contador_global'.
#   # contador_global = 20 # Esto crearía una variable LOCAL diferente

#   # Para MODIFICAR la variable GLOBAL 'contador_global' desde dentro de la función,
#   # necesitamos usar la palabra clave 'global'.
#   global contador_global
#   contador_global = 20 # Ahora SÍ estamos modificando la variable GLOBAL

#   print(f"Dentro de la función (después de cambiar): {contador_global}")

# # Imprimimos el valor global antes de la llamada a la función
# print(f"Fuera de la función (antes de la llamada): {contador_global}")

# # Llamamos a la función para que intente cambiar el valor
# incrementar_contador()

# # Imprimimos el valor global después de la llamada a la función
# print(f"Fuera de la función (después de la llamada): {contador_global}")




print("--------------------------------------------")
def get_average_score(scores):
  return (scores["spanish_score"] + scores["science_score"] + scores["history_score"]) / 3


def is_student_exempted(scores):
  return scores["average_score"] > 70


# Scores
students = [
  {
    "name": "Juan",
		"spanish_score": 75,
		"science_score": 95,
		"history_score": 54,
	},
  {
    "name": "Sofia",
		"spanish_score": 64,
		"science_score": 56,
		"history_score": 98,
	},
  {
    "name": "Paul",
		"spanish_score": 72,
		"science_score": 75,
		"history_score": 79,
	}
]

# Averages
for student in students:
  student["average_score"] = get_average_score(student)
  student["is_exempted"] = is_student_exempted(student)
  print(student["name"], " is_exempted is ", student["is_exempted"])


print("----------------------------")

print("//////////////")

def saludar_a_alguien():
  print("¡Hola! ¿Cómo estás?")
  despedirse_cordialmente() # Aquí la primera función llama a la segunda

def despedirse_cordialmente():
  print("¡Hasta luego! Que tengas un excelente día.")

def principal():
  print("Iniciando el programa...")
  saludar_a_alguien() # La función principal llama a la primera función
  print("Programa finalizado.")

if __name__ == "__main__":
  principal()



print("//////////////")

print("//////////////")


# 2. Experimente con el concepto de scope:
#     1. Intente accesar a una variable definida dentro de una función desde afuera.
#     2.  Intente accesar a una variable global desde una función y cambiar su valor

def mi_funcion():
    mensaje_local = "Hola desde la función!"
    print(mensaje_local) # Esto funciona porque estamos dentro de la función

# Intentamos acceder a mensaje_local desde fuera de la función
# Esto generará un error NameError
try:
    print(mensaje_local)
except NameError as e:
    print(f"Error: {e}. No se puede acceder a 'mensaje_local' fuera de 'mi_funcion' porque es una variable local.")

mi_funcion()



#     mensaje_local = "Hola desde la función!"
#     print(mensaje_local) # Esto funciona porque estamos dentro de la función

# # --- Experimentando el concepto de Scope ---

# # Intento 1: Acceder a una variable definida dentro de una función desde afuera.
# # ESTE CÓDIGO CAUSARÍA UN NameError si no estuviera comentado.
# # Python buscaría 'mensaje_local' en el ámbito global y no la encontraría.
# # print(mensaje_local)

# mi_funcion()

print("*****************")
saldo_global = 100 # Esta es una variable global

def depositar(cantidad):
    global saldo_global # Indicamos que vamos a modificar la variable global 'saldo_global'
    print(f"Saldo actual antes del depósito (dentro de la función): ${saldo_global}")
    saldo_global += cantidad
    print(f"Saldo después del depósito (dentro de la función): ${saldo_global}")

def retirar(cantidad):
    global saldo_global
    # Sin 'global', esto crearía una nueva variable local 'saldo_global'
    # si intentaras reasignar directamente.
    # Para solo leerla, no necesitas 'global'.
    print(f"Intentando retirar ${cantidad} de un saldo de ${saldo_global}")
    if saldo_global >= cantidad:
        # Para modificar, necesitamos 'global' aquí también.
        # Si no la ponemos, Python asume que 'saldo_global' es una variable local no inicializada
        # si intentas modificarla.
        # Descomenta la línea de abajo para ver el efecto de no usar 'global' si intentas modificar:
        # saldo_global -= cantidad # Esto daría un UnboundLocalError si no se usa global
        # Para que funcione correctamente y modifique la global:
        
        saldo_global -= cantidad
        print("Retiro exitoso.")
    else:
        print("Fondos insuficientes.")

print(f"Saldo inicial (global): ${saldo_global}")

depositar(50)
print(f"Saldo después del depósito (fuera de la función): ${saldo_global}")

retirar(30)
print(f"Saldo después del retiro (fuera de la función): ${saldo_global}")

retirar(150) # Intentar retirar más de lo que hay
print(f"Saldo final (fuera de la función): ${saldo_global}")



print("//////////////")

print("//////////////")

print("//////////////")

# 3. Cree una función que retorne la suma de todos los números de una lista.
#     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#     2. [4, 6, 2, 29] → 41



def sumar_elementos_lista(numeros):
    """
    Esta función toma una lista de números y retorna su suma total.

    Parámetros:
    numeros (list): Una lista que contiene números (enteros o flotantes).

    Retorna:
    int/float: La suma de todos los elementos de la lista.
    """
    suma_total = 0 # Inicializamos una variable para guardar la suma

    # Iteramos sobre cada número en la lista 'numeros'
    for numero in numeros:
        suma_total += numero # Sumamos cada número a nuestra variable suma_total

    return suma_total # Devolvemos el resultado final

# --- Ejemplos de uso ---
mi_lista_1 = [1, 2, 3, 4, 5]
resultado_1 = sumar_elementos_lista(mi_lista_1)
print(f"La suma de los elementos de {mi_lista_1} es: {resultado_1}") # Salida: 15

mi_lista_2 = [10, 20, 30]
resultado_2 = sumar_elementos_lista(mi_lista_2)
print(f"La suma de los elementos de {mi_lista_2} es: {resultado_2}") # Salida: 60

mi_lista_3 = [-1, 0, 1]
resultado_3 = sumar_elementos_lista(mi_lista_3)
print(f"La suma de los elementos de {mi_lista_3} es: {resultado_3}") # Salida: 0

lista_vacia = []
resultado_vacia = sumar_elementos_lista(lista_vacia)
print(f"La suma de los elementos de {lista_vacia} es: {resultado_vacia}") # Salida: 0 (la suma de una lista vacía es 0)

print("//////////////")

print("//////////////")

print("//////////////")

print("//////////////")
# 4. Cree una función que le de la vuelta a un string y lo retorne.
#     1. Esto ya lo hicimos en iterables.
#     2. “Hola mundo” → “odnum aloH”

def invertir_string(cadena):
    """
    Esta función toma una cadena de texto y retorna la cadena invertida.

    Parámetros:
    cadena (str): La cadena de texto que se desea invertir.

    Retorna:
    str: La cadena de texto invertida.
    """
    return cadena[::-1] # Usamos un truco de Python para invertir la cadena

# --- Ejemplos de uso ---
texto_original_1 = "Hola mundo"
texto_invertido_1 = invertir_string(texto_original_1)
print(f"Original: '{texto_original_1}' -> Invertido: '{texto_invertido_1}'") # Salida: 'odnum aloH'

texto_original_2 = "Python"
texto_invertido_2 = invertir_string(texto_original_2)
print(f"Original: '{texto_original_2}' -> Invertido: '{texto_invertido_2}'") # Salida: 'nohtyP'

texto_original_3 = "Anita lava la tina"
texto_invertido_3 = invertir_string(texto_original_3)
print(f"Original: '{texto_original_3}' -> Invertido: '{texto_invertido_3}'") # Salida: 'anit al aval itinA'

texto_vacio = ""
texto_invertido_vacio = invertir_string(texto_vacio)
print(f"Original: '{texto_vacio}' -> Invertido: '{texto_invertido_vacio}'") # Salida: ''


print("***********************")
print("***********************")


# 4. Cree una función que le de la vuelta a un string y lo retorne.
#     1. Esto ya lo hicimos en iterables.
#     2. “Hola mundo” → “odnum aloH”



def invertir_string_manual(cadena):
    """
    Esta función toma una cadena de texto y retorna la cadena invertida,
    construyéndola caracter por caracter usando un bucle.

    Parámetros:
    cadena (str): La cadena de texto que se desea invertir.

    Retorna:
    str: La cadena de texto invertida.
    """
    cadena_invertida = "" # 1. Inicializamos una cadena vacía para construir el resultado

    # 2. Iteramos sobre la cadena original desde el último caracter hasta el primero
    # len(cadena) - 1 es el índice del último caracter
    # -1 es el índice hasta el que queremos llegar (justo antes del -1, es decir, el índice 0)
    # -1 es el paso, lo que significa que vamos hacia atrás
    for indice in range(len(cadena) - 1, -1, -1):
        caracter = cadena[indice] # 3. Obtenemos el caracter en la posición actual
        cadena_invertida += caracter # 4. Añadimos el caracter al final de nuestra nueva cadena

    return cadena_invertida # 5. Retornamos la cadena invertida

# --- Ejemplos de uso ---
texto_original_1 = "Hola mundo"
texto_invertido_1 = invertir_string_manual(texto_original_1)
print(f"Original: '{texto_original_1}' -> Invertido: '{texto_invertido_1}'") # Salida: 'odnum aloH'

texto_original_2 = "Python"
texto_invertido_2 = invertir_string_manual(texto_original_2)
print(f"Original: '{texto_original_2}' -> Invertido: '{texto_invertido_2}'") # Salida: 'nohtyP'

texto_original_3 = "Anita lava la tina"
texto_invertido_3 = invertir_string_manual(texto_original_3)
print(f"Original: '{texto_original_3}' -> Invertido: '{texto_invertido_3}'") # Salida: 'anit al aval itinA'

texto_vacio = ""
texto_invertido_vacio = invertir_string_manual(texto_vacio)
print(f"Original: '{texto_vacio}' -> Invertido: '{texto_invertido_vacio}'") # Salida: ''




print("//////////////")

print("//////////////")

print("//////////////")

print("//////////////")

print("//////////////")

# 5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#     1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”


def contar_mayusculas_minusculas(cadena):
    """
    Esta función cuenta el número de letras mayúsculas y minúsculas en un string
    e imprime el resultado.

    Parámetros:
    cadena (str): La cadena de texto a analizar.
    """
    mayusculas = 0  # Inicializamos el contador de letras mayúsculas
    minusculas = 0  # Inicializamos el contador de letras minúsculas

    # Iteramos sobre cada caracter en la cadena
    for caracter in cadena:
        if caracter.isupper():  # Verificamos si el caracter es una letra mayúscula
            mayusculas += 1     # Si lo es, incrementamos el contador de mayúsculas
        elif caracter.islower(): # Verificamos si el caracter es una letra minúscula
            minusculas += 1     # Si lo es, incrementamos el contador de minúsculas
        # Si el caracter no es ni mayúscula ni minúscula (ej. espacios, números, símbolos),
        # simplemente lo ignoramos y no incrementamos ningún contador.

    # Imprimimos el resultado con el formato solicitado
    print(f"There's {mayusculas} upper cases and {minusculas} lower cases")

# --- Ejemplos de uso ---
print("Ejemplo 1:")
contar_mayusculas_minusculas("I love Nación Sushi") # Salida: There's 3 upper cases and 13 lower cases

print("\nEjemplo 2:")
contar_mayusculas_minusculas("PyThOn 3.10") # Salida: There's 3 upper cases and 2 lower cases

print("\nEjemplo 3:")
contar_mayusculas_minusculas("HOLA MUNDO!") # Salida: There's 9 upper cases and 0 lower cases

print("\nEjemplo 4:")
contar_mayusculas_minusculas("hola mundo") # Salida: There's 0 upper cases and 9 lower cases

print("\nEjemplo 5:")
contar_mayusculas_minusculas("12345 !@#$") # Salida: There's 0 upper cases and 0 lower cases



print("//////////////")

print("//////////////")

print("//////////////")

print("//////////////")

print("//////////////")

print("//////////////")

# 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#     1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#     2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”


def ordenar_palabras_en_string(string_con_guiones):
    """
    Esta función toma un string de palabras separadas por guiones,
    las ordena alfabéticamente y retorna un nuevo string con las palabras ordenadas,
    también separadas por guiones.

    Parámetros:
    string_con_guiones (str): La cadena de texto con palabras separadas por guiones.

    Retorna:
    str: La cadena de texto con las palabras ordenadas alfabéticamente.
    """
    # 1. Convertir el string a una lista de palabras
    # El método .split('-') divide el string donde encuentra el guión y crea una lista.
    lista_palabras = string_con_guiones.split('-')

    # 2. Ordenar la lista de palabras alfabéticamente
    # El método .sort() ordena la lista en su lugar (modifica la lista original).
    lista_palabras.sort()

    # 3. Convertir la lista de palabras de nuevo a un string
    # El método .join('-') une los elementos de la lista usando el guión como separador.
    string_ordenado = '-'.join(lista_palabras)

    return string_ordenado # Retornamos el string final ordenado

# --- Ejemplos de uso ---
print("Ejemplo 1:")
texto_original_1 = "python-variable-funcion-computadora-monitor"
texto_ordenado_1 = ordenar_palabras_en_string(texto_original_1)
print(f"Original: '{texto_original_1}'")
print(f"Ordenado: '{texto_ordenado_1}'")
# Salida: 'computadora-funcion-monitor-python-variable'

print("\nEjemplo 2:")
texto_original_2 = "manzana-pera-platano-uva-naranja"
texto_ordenado_2 = ordenar_palabras_en_string(texto_original_2)
print(f"Original: '{texto_original_2}'")
print(f"Ordenado: '{texto_ordenado_2}'")
# Salida: 'manzana-naranja-pera-platano-uva'

print("\nEjemplo 3:")
texto_original_3 = "z-b-a-c"
texto_ordenado_3 = ordenar_palabras_en_string(texto_original_3)
print(f"Original: '{texto_original_3}'")
print(f"Ordenado: '{texto_ordenado_3}'")
# Salida: 'a-b-c-z'

print("\nEjemplo 4: String vacío")
texto_original_4 = ""
texto_ordenado_4 = ordenar_palabras_en_string(texto_original_4)
print(f"Original: '{texto_original_4}'")
print(f"Ordenado: '{texto_ordenado_4}'")
# Salida: '' (un string vacío produce un string vacío ordenado)

print("\nEjemplo 5: Una sola palabra")
texto_original_5 = "única"
texto_ordenado_5 = ordenar_palabras_en_string(texto_original_5)
print(f"Original: '{texto_original_5}'")
print(f"Ordenado: '{texto_ordenado_5}'")
# Salida: 'única' (una sola palabra no cambia al ordenarse) 





print("//////////////")

print("//////////////")

print("//////////////")

print("//////////////")

print("//////////////")

print("//////////////")

print("//////////////")
# 7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#     1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#     2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, 
# y conviertala a codigo. No busque el codigo, eso no ayudaria.


def encontrar_primos_en_lista(numeros):
    """
    Esta función toma una lista de números y retorna una nueva lista
    que contiene solo los números primos de la lista original.

    Parámetros:
    numeros (list): Una lista de números enteros.

    Retorna:
    list: Una nueva lista que contiene solo los números primos.
    """
    numeros_primos = [] # Creamos una lista vacía para almacenar los números primos encontrados

    # Iteramos sobre cada número en la lista de entrada
    for numero in numeros:
        # Un número primo debe ser mayor que 1.
        # Los números 0, 1 y negativos no son primos.
        if numero <= 1:
            continue # Si no es mayor que 1, pasamos al siguiente número en la lista

        # Asumimos que el número es primo hasta que encontremos un divisor
        es_primo = True

        # Verificamos divisores desde 2 hasta la raíz cuadrada del número (optimización).
        # Para simplificar y seguir una lógica más directa para tu nivel actual,
        # vamos a verificar divisores desde 2 hasta (numero - 1).
        # Si un número es divisible por alguno de estos, no es primo.
        for i in range(2, numero): # Itera desde 2 hasta numero-1
            if numero % i == 0: # Si el resto de la división es 0, es divisible
                es_primo = False # Encontramos un divisor, así que no es primo
                break # No necesitamos seguir buscando, ya sabemos que no es primo

        # Si después de revisar todos los posibles divisores, 'es_primo' sigue siendo True,
        # significa que el número es primo y lo agregamos a nuestra lista.
        if es_primo:
            numeros_primos.append(numero)

    return numeros_primos # Devolvemos la lista final de números primos

# --- Ejemplos de uso ---
print("Ejemplo 1:")
mi_lista_1 = [1, 4, 6, 7, 13, 9, 67, 2, 0, -5]
primos_encontrados_1 = encontrar_primos_en_lista(mi_lista_1)
print(f"Lista original: {mi_lista_1}")
print(f"Números primos: {primos_encontrados_1}") # Salida: [7, 13, 67, 2]

print("\nEjemplo 2:")
mi_lista_2 = [29, 31, 33, 37, 40]
primos_encontrados_2 = encontrar_primos_en_lista(mi_lista_2)
print(f"Lista original: {mi_lista_2}")
print(f"Números primos: {primos_encontrados_2}") # Salida: [29, 31, 37]

print("\nEjemplo 3:")
lista_vacia = []
primos_encontrados_vacia = encontrar_primos_en_lista(lista_vacia)
print(f"Lista original: {lista_vacia}")
print(f"Números primos: {primos_encontrados_vacia}") # Salida: []

print("\nEjemplo 4: Números sin primos")
lista_sin_primos = [4, 8, 10, 15]
primos_encontrados_sin = encontrar_primos_en_lista(lista_sin_primos)
print(f"Lista original: {lista_sin_primos}")
print(f"Números primos: {primos_encontrados_sin}") # Salida: []