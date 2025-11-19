#7 Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos.
#  Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”.
# Si es exactamente igual, muestre “Igual”.



tiempo_en_segundos=int(input(f"porfavor ingrese su tiempo en segundos= "))

if tiempo_en_segundos<600:
    segundos_faltantes=600-tiempo_en_segundos
    print(f" faltan {segundos_faltantes} para llegar a 10 minutos ")
elif tiempo_en_segundos>600:
    print(f" mayor")
else:
    print(f" igual")