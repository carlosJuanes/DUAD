#8 Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado.
#  Luego muestre el resultado de la suma.

contador=1
resultado=0
numero_ingresado=int(input(f"ingrese su numero= "))
while contador<=numero_ingresado:
    resultado=resultado+contador
    contador=contador+1
print(f" el resultado es de = {resultado}")