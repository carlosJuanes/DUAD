#17  Cree un algoritmo que le pida 100 números al usuario y muestre el mayor de todos.

contador=1
numeros_totales=5
numero_mayor=float(input(f"porfavor ingrese el numero {contador}= "))

while contador<numeros_totales:
    contador+=1
    numero_ingresado=float(input(f"porfavor ingrese el numero {contador}= "))
    if numero_ingresado>numero_mayor:
        numero_mayor=numero_ingresado
print(f"el numero mayor es {numero_mayor}")
