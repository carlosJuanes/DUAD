#13 Cree un algoritmo que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”.
#  Sino, mostrar “incorrecto”.

suma_total=30
numero_1=int(input("ingrese su primer numero: "))
numero_2=int(input("ingrese su segundo numero: "))
numero_3=int(input("ingrese su tercer numero: "))

if (numero_1==30)or(numero_2==30)or(numero_3==30)or(numero_1+numero_2+numero_3==suma_total):
    print("CORRECTO")
else:
    print("INCORRECTO")
