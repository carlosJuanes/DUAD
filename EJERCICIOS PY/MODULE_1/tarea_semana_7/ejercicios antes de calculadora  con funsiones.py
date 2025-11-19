# def saludar_usuario():
#     print("¡Hola, bienvenido a mi programa!")

# saludar_usuario()


# def sumar_dos_numeros(num1,num2):
#     print(num1+num2)

# sumar_dos_numeros(5,5)
# sumar_dos_numeros(50,50)


# def restar_numeros(num1,num2,):
#     return num1-num2

# resta=restar_numeros(25,20)
# print(resta)


def obtener_numero_valido():
    while True:
        numero_ingresado=input("Por favor, ingresa un número:")
        try:
            numero_float=float(numero_ingresado)
            return(numero_float)
        except ValueError:
            print("¡Error! Eso no es un número válido. Intenta de nuevo.")
conversion_de_numero=obtener_numero_valido()

print(conversion_de_numero)