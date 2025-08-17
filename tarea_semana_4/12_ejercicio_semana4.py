#12  Cree un algoritmo  que tenga un numero secreto del 1 al 10, y le pida al usuario adivinar ese número.
#  El algoritmo no debe terminar hasta que el usuario adivine el numero.


numero_secreto=7

numero_ingresado= int(input("ingrese un numero del 1 - 10 = "))
while numero_ingresado!=numero_secreto:
    print("INCORRECTO, porfavor vuelva a intentarlo")
    numero_ingresado= int(input("ingrese un numero del 1 - 10 = "))
print(f"FELICIDADES!!! el numero secreto es {numero_secreto}")