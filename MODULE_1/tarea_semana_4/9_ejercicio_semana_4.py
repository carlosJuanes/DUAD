#Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas (primero y segundo)
#  y los ordene de menor a mayor en dichas variables.

primer_numero=int(input(f"ingrese su primer numero= "))
segundo_numero=int(input(f"ingrese su segundo numero= "))

if primer_numero>segundo_numero:
    print(f"{segundo_numero} {primer_numero}")
else:
    print(f"{primer_numero} {segundo_numero}")
    