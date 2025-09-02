#2 Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un 
# bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
nombre=input("ingrese su nombre")
apellido=input("ingrese sus apellidos")
edad=int(input("ingrese su edad"))

if edad<=2:
    print(f"{nombre} {apellido}, edad {edad} bebe")
elif edad<=6:
    print(f"{nombre} {apellido}, edad {edad} niño(a)")
elif edad<=12:
    print(f"{nombre} {apellido}, edad {edad} pre-adolecente")
elif edad<=20:
    print(f"{nombre} {apellido}, edad {edad} adolecente")
elif edad<=40:
    print(f"{nombre} {apellido}, edad {edad} adulto joven")
elif edad<=65:
    print(f"{nombre} {apellido}, edad {edad} adulto")
elif edad>65:
    print(f"{nombre} {apellido}, edad {edad} adulto mayor")