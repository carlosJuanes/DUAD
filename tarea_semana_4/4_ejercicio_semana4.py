#4. Cree un programa que le pida tres números al usuario y muestre el mayor.


primer_numero=int(input("ingrese su primer numero"))
segundo_numero=int(input("ingrese su segundo numero"))
tercer_numero=int(input("ingrese su tercer numero"))

numero_mayor=primer_numero
if segundo_numero>primer_numero:
    numero_mayor=segundo_numero
if tercer_numero>numero_mayor:
    numero_mayor=tercer_numero
print(f"el numero mayor es {numero_mayor}")
