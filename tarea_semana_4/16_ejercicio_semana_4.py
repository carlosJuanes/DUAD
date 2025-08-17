# 16 Cree un algoritmo que le pida 100 números al usuario y muestre la suma de todos.

contador=1
numeros_totales=5
numero_mayor=float(input(f" porfavor ingresa el numero {contador} = "))

while contador<numeros_totales:
    contador=contador+1
    numero_actual=float(input(f" ingrese el numero {contador}= "))
    if numero_actual>numero_mayor:
        numero_mayor=numero_actual
print(f"el numero mayor es  {numero_mayor}")
