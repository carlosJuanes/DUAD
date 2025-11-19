#14 Cree un diagrama de flujo que le pida 5 números al usuario y muestre el mayor.

primer_numero=float(input("Ingrese el primer numero= "))
numero_mayor=primer_numero

segundo_numero=float(input("ingrese el segundo numero= "))
if segundo_numero>numero_mayor:
    numero_mayor=segundo_numero

tercer_numero=float(input("Ingrese el tercer numero"))
if tercer_numero>numero_mayor:
    numero_mayor=tercer_numero

cuarto_numero=float(input("ingrese el cuarto numero"))
if cuarto_numero>numero_mayor:
    numero_mayor=cuarto_numero

quinto_numero=float(input("Ingrese el quinto numero= "))
if quinto_numero>numero_mayor:
    numero_mayor=quinto_numero

print(f" El numero mayor es {numero_mayor}")
