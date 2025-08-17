# # Ejercicio 1: Conversor de Temperatura Robusto
# while True:
#     try:
#         pedir_grados_celcius=input(f"por favor ingrese la temperatura en grados celcius")
#         celcius=float(pedir_grados_celcius)
#         fahrenheit=(celcius*9)/5+32
#         print(f"la convercion de temperatura de celcius a fahrenheit es de {fahrenheit:.2f} grados fahrenheit")
#         break
#     except ValueError:
#         print(f"hubo un error")


# """Ejercicio 2: Menú Interactivo de Operaciones Básicas
# Ahora que dominas la validación de entrada, vamos a aplicar lo aprendido y añadir más lógica con estructuras condicionales 
# para un menú.
# Objetivo: Practicar el uso de bucles para menús, estructuras condicionales (if/elif/else) y la ejecución repetida de acciones.
# Descripción: Escribe un programa que muestre un menú con tres opciones:
# "Saludar
# "Decir adiós"
# "Salir del programa"
# El programa debe pedir al usuario que elija una opción. 
# Si elige "Saludar", debe imprimir "¡Hola!". Si elige "Decir adiós", debe imprimir "¡Hasta luego!".
# Si elige "Salir del programa", el programa debe terminar. Si el usuario ingresa una opción inválida, 
# debe mostrar un mensaje de error y volver a mostrar el menú.
# Pistas:
# Usa un bucle while (podría ser un while True) para mantener el menú mostrándose continuamente.
# Dentro del bucle, usa input() para obtener la opción del usuario.
# Emplea if, elif y else para manejar las diferentes opciones y la entrada inválida.
# Si el usuario elige la opción de "Salir", usa la palabra clave break para salir del bucle while y terminar el programa.
# Considera cómo puedes hacer que la entrada del usuario para las opciones sea flexible (por ejemplo, si ingresa "1" o "uno").
# Por ahora, puedes centrarte en los números.
# Tómate tu tiempo para construir este programa. Cuando lo tengas listo, o si te surge alguna duda, ¡no dudes en consultarme!"""

# while True:
#     try:
#         entrada=int(input("porfavor seleccione una opcion 1= saludar, 2= decir adios, 3= salir del programa"))
#         if entrada==1:
#             print("hola!")
#         elif entrada==2:
#             print("hasta luego")
#         elif entrada==3:
#             break
#         else:
#             print("seleccione una opcion valida")
#     except ValueError:
#         print("hubo un error seleccione una entrada valida")



# numero_actual=0

# while True:
#     print(f"= {numero_actual}")
#     sumar_numero= input("ingrese el numero a sumar o (salir) para salir del programa")
#     sumar_numero=sumar_numero.lower()
#     if sumar_numero=="salir":
#         break
#     try:
#         numero_float=float(sumar_numero)
#         numero_actual+=numero_float
#         print(numero_actual)
#     except ValueError:
#         print("porfavor ingrese un numero valido")



"""CALCULADORA"""

numero_actual=0.0
while True:
    print("---------------------")
    print("    CALCULADORA")
    print("---------------------")

    print(f"{numero_actual}")
    print(f"que desea hacer:\n"
        f"1= Sumar\n"
        f"2= Restar\n"
        f"3= Multiplicar\n"
        f"4= Dividir\n"
        f"5= Borrar resultado\n"
        f"6= Salir") 
    
    operacion=input(f"seleccione una opcion ")
    
    try:
        operacion_num=int(operacion)
        if operacion_num==1:
            try:
                sumar_numero=float(input(f"ingrese el numero a sumar {numero_actual}+ "))
                numero_actual+=sumar_numero
                print(f"={numero_actual}")
            except ValueError:
                print("¡error! ingrese un numero valido")
        elif operacion_num==2:
            try:
                restar_numero=float(input(f"ingrese el numero a restar {numero_actual}- "))
                numero_actual=numero_actual-restar_numero
                print(f"={numero_actual}")
            except ValueError:
                print("¡error! ingrese un numero valido")
        elif operacion_num==3:
            try:
                multiplicar_numero=float(input(f"ingrese el numero a multiplicar {numero_actual}* "))
                numero_actual=numero_actual*multiplicar_numero
                print(f"={numero_actual}")
            except ValueError:
                print("¡error! ingrese un numero valido")
        elif operacion_num==4:
            try:
                dividir_numero=float(input(f"ingrese el numero a dividir {numero_actual}/ "))
                numero_actual=numero_actual/dividir_numero
                print(f"={numero_actual}")
            except ZeroDivisionError:
                print("¡error! error al dividir entre cero")
        elif operacion_num==5:
            numero_actual=0.0
            print(f"{numero_actual}")
            print("ingrese un numero")
        elif operacion_num==6:
            print("saliendo de la calculadora")
            break
        else:
            print(" opcion no valida, porfavor ingrese un numero del 1-6")
    except ValueError:
        print("ingrese un valor valido")




# print("--------------------------------------")
# """CALCULADORA"""

# numero_actual = 0.0 # Es buena práctica inicializarlo como float si vas a operar con floats

# while True:
#     print(f"\n--- Calculadora ---")
#     print(f"Número actual: {numero_actual:.2f}") # Formatear para 2 decimales
#     print("-------------------")
#     operacion = input(f"Seleccione una opción:\n"
#                       f"1= Sumar\n"
#                       f"2= Restar\n"
#                       f"3= Multiplicar\n"
#                       f"4= Dividir\n"
#                       f"5= Borrar resultado\n"
#                       f"6= Salir\n"
#                       f"Su opción: ")

#     operacion_lower = operacion.lower()

#     if operacion_lower == "salir":
#         print("Saliendo de la calculadora. ¡Adiós!")
#         break # Sale del bucle principal

#     try:
#         operacion_num = int(operacion) # Convertir la opción a entero

#         if operacion_num == 1: # Suma
#             try:
#                 segundo_numero = float(input(f"Ingrese el número a sumar a {numero_actual}: "))
#                 numero_actual += segundo_numero
#                 print(f"Resultado: {numero_actual:.2f}")
#             except ValueError:
#                 print("¡Error! Por favor, ingrese un número válido.")
        
#         elif operacion_num == 2: # Resta
#             try:
#                 segundo_numero = float(input(f"Ingrese el número a restar de {numero_actual}: "))
#                 numero_actual -= segundo_numero
#                 print(f"Resultado: {numero_actual:.2f}")
#             except ValueError:
#                 print("¡Error! Por favor, ingrese un número válido.")

#         elif operacion_num == 3: # Multiplicación
#             try:
#                 segundo_numero = float(input(f"Ingrese el número para multiplicar por {numero_actual}: "))
#                 numero_actual *= segundo_numero
#                 print(f"Resultado: {numero_actual:.2f}")
#             except ValueError:
#                 print("¡Error! Por favor, ingrese un número válido.")

#         elif operacion_num == 4: # División
#             try:
#                 segundo_numero = float(input(f"Ingrese el número para dividir {numero_actual} entre: "))
#                 if segundo_numero == 0: # Validar división por cero antes de que ocurra el error
#                     print("¡Error! No se puede dividir por cero.")
#                 else:
#                     numero_actual /= segundo_numero
#                     print(f"Resultado: {numero_actual:.2f}")
#             except ValueError:
#                 print("¡Error! Por favor, ingrese un número válido.")
#             # El ZeroDivisionError también podría ir aquí, pero la verificación 'if' es más específica
#             # except ZeroDivisionError: 
#             #     print("¡Error! No se puede dividir por cero.")

#         elif operacion_num == 5: # Borrar resultado
#             numero_actual = 0.0 # Restablecer a 0.0 para mantener el tipo float
#             print("El resultado ha sido borrado. Número actual: 0.00")
#             # No se necesita try-except aquí porque no hay input que pueda fallar en la conversión.

#         elif operacion_num == 6: # La opción de salir numérica
#             # Aunque ya manejamos "salir" por texto, podemos reafirmarlo aquí.
#             print("Saliendo de la calculadora. ¡Adiós!")
#             break

#         else: # Opción numérica fuera del rango 1-6
#             print("Opción inválida. Por favor, ingrese un número del 1 al 6 o 'salir'.")

#     except ValueError:
#         # Esto captura si el usuario no ingresa un número para la opción del menú
#         print("Entrada inválida para la opción. Por favor, ingrese un número (1-6) o 'salir'.")
