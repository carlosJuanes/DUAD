# 1- Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def mezclar_colores():
    print("blanco  y negro")
    resultado()


def resultado():
    print("gris")


def main():
    mezclar_colores()

main()

print()
print()
# 2. Experimente con el concepto de scope:
#    Intente accesar a una variable definida dentro de una función desde afuera.


def name():
    my_name="Carlos Juanes"
    print(my_name)


# print(my_name)
print()
#Intente accesar a una variable global desde una función y cambiar su valor. 

puntos_totales=0

def aumentar(puntos):
    global puntos_totales
    print(f"Puntos totales antes del aumento de puntos {puntos_totales}")
    puntos_totales+=puntos
    print(f"Punto totales despues del aumento de puntos {puntos_totales}")


def disminuir(puntos):
    global puntos_totales
    print(f"puntos totales antes de disminuir puntos {puntos_totales}")
    puntos_totales-=puntos
    print(f"puntos totales despues de disminuir puntos {puntos_totales}")


print(f"puntuacion inicial global {puntos_totales}")

aumentar(10)

disminuir(5)

print()
print()
# 3. Cree una función que retorne la suma de todos los números de una lista.
#     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#     2. [4, 6, 2, 29] → 41

def suma_de_numeros(numeros):
    suma_total=0
    for numero in numeros:
        suma_total+=numero
    return suma_total
my_list=[4,6,2,29]
suma=suma_de_numeros(my_list)
print(f"lista de numeros={my_list} suma de la lista de numeros {suma}")
print()
print()

# 4. Cree una función que le de la vuelta a un string y lo retorne.
#     1. Esto ya lo hicimos en iterables.
#     2. “Hola mundo” → “odnum aloH”

def invertir_palabra(palabra):
    palabra_invertida=""
    for index in range(len(palabra)-1,-1,-1):
        letra=palabra[index]
        palabra_invertida+=letra
    return palabra_invertida

mi_palabra="hola mundo"
invertir=invertir_palabra(mi_palabra)
print(f"palabra original {mi_palabra}, palabra invertida={invertir}")
print()
print()
# 5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#     1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def contador_de_mayusculas_minusculas(palabra):
    mayuscula=0
    minuscula=0
    for letra in palabra:
        if letra.isupper():
            mayuscula+=1
        elif letra.islower():
            minuscula+=1
    print(f"cadena there´s {mayuscula} upper cases  and {minuscula} lower cases")

contador_de_mayusculas_minusculas("I love Nation Sushi")
print()
print()
# 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#     1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#     2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

def ordenar_alfabeticamente(string_con_guiones):
    lista_de_palabras=string_con_guiones.split("_")
    lista_de_palabras.sort()
    string_ordenado="_".join(lista_de_palabras)
    return string_ordenado

mi_string_con_guines="may_the_force_be_with_you"
string_orden_alfabetico=ordenar_alfabeticamente(mi_string_con_guines)
print(f"texto con guiones {mi_string_con_guines}")
print(f"texto ordenado alfabeticamente {string_orden_alfabetico}")

print()
print()

# 7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#     1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#     2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, 
# y conviertala a codigo. No busque el codigo, eso no ayudaria.
#     3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo,
#  y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*

def ordenar_numeros_primos(numeros):
    numeros_primos=[]

    for numero in  numeros:
        if numero<=1:
            continue
        es_primos=True

        for index in range(2,numero):
            if numero %index==0:
                es_primos=False
                break
        if es_primos:
            numeros_primos.append(numero)
    return numeros_primos

lista_de_numeros= [1,2,3,4,5,6,7,8,9,11,52,36,5,748,5,4,6,2,1,-4,-55,7,77,7777,4]
numeros_primos_encontrados=ordenar_numeros_primos(lista_de_numeros)

print(f"lista original {lista_de_numeros}")
print(f"numeros primos encontrados {numeros_primos_encontrados}")

print()
print()

# 1. Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto
#     - Ejemplo:
#         - texto = "programacion"
#         - carácter = "o"
#     - Resultado → 2


def contador_de_caracteres(texto,caracter):
    contador=0
    for letra in texto:
        if letra==caracter:
            contador+=1
    return contador

mi_texto="programacion"
mi_caracter="o"
resultado_total=contador_de_caracteres(mi_texto,mi_caracter)
print (f"el caracter {mi_caracter}  aparece {resultado_total} veces en {mi_texto}")



print()
print()

# 2. Cree una función que reciba una lista de palabras y un número `n`,
#  y retorne una nueva lista con solo las palabras que tengan más de `n` letras
#     - Ejemplo:
#         - palabras = `["cielo", "sol", "maravilloso", "día"]`
#         - n = 4
#     - Resultado → `["cielo", "maravilloso"]`


def clasificar_palabras(lista_de_palabras,numero):
    nueva_lista_de_palabras=[]
    for palabra in lista_de_palabras:
        len(palabra)
        if len(palabra)>numero:
            nueva_lista_de_palabras.append(palabra)
    return nueva_lista_de_palabras

palabras_a_contar=["cielo","sol","perro","gato","extraterrestre","luz","uno"]
n=4
encontrar_las_palabras=clasificar_palabras(palabras_a_contar,n)
print(f"lista orignal {palabras_a_contar}")
print(f"las palabras con mas de {n} letras son: {encontrar_las_palabras}")


print()
print()


# 3. Cree una función que reciba un string y retorne cuántas vocales contiene
#     - Ejemplo:
#         - frase = `Hola mundo`
#     - Resultado → `4`

def contador_de_vocales(texto):
    contador=0
    for letra in texto:
        if letra.lower() in "aeiou":
            contador+=1
    return contador

my_texto="hola mundo"
conclusion=contador_de_vocales(my_texto)
print(f"la palabra {my_texto} contiene {conclusion} vocales")