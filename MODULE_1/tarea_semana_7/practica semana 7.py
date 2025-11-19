# def pedir_numero():
#     while True: # Bucle infinito que se repetirá hasta que se rompa explícitamente
#         try:
#             entrada = input("Por favor, ingresa un número: ")
#             numero = int(entrada) # Intenta convertir a entero
#             print(f"¡Excelente! Ingresaste el número: {numero}")
#             break # Si la conversión es exitosa, salimos del bucle
#         except ValueError:
#             # Si ocurre un ValueError, imprimimos el mensaje y el bucle vuelve a empezar
#             print("Eso no es un número válido. Por favor, intenta de nuevo.")
#         except Exception as e:
#             # Captura cualquier otra excepción inesperada
#             print(f"Ocurrió un error inesperado: {e}. Por favor, intenta de nuevo.")

# # Llamamos a la función
# pedir_numero()
# print("El programa ha continuado después de obtener un número válido.")

# print()
# print()
# def pedir_numero():
#     while True: # Bucle infinito que se repetirá hasta que se rompa explícitamente
#         try:
#             entrada = input("Por favor, ingresa un número: ")
#             numero = int(entrada) # Intenta convertir a entero
#             print(f"¡Excelente! Ingresaste el número: {numero}")
#             break # Si la conversión es exitosa, salimos del bucle
#         except ValueError:
#             # Si ocurre un ValueError, imprimimos el mensaje y el bucle vuelve a empezar
#             print("Eso no es un número válido. Por favor, intenta de nuevo.")
#         except Exception as e:
#             # Captura cualquier otra excepción inesperada
#             print(f"Ocurrió un error inesperado: {e}. Por favor, intenta de nuevo.")

# # Llamamos a la función
# pedir_numero()
# print("El programa ha continuado después de obtener un número válido.")


# print()
# print()
# def calificar_examen(puntuacion):
#     if puntuacion < 0:
#         # Si la puntuación es negativa, ¡es un error para nosotros!
#         raise ValueError("La calificación no puede ser un número negativo.")
#     print(f"Calificación registrada: {puntuacion}")

# # Uso:
# try:
#     calificar_examen(85)
#     calificar_examen(-10) # Esto lanzará el ValueError
# except ValueError as e:
#     print(f"Error: {e}")

print()
print()
def comprar_producto(stock_actual, cantidad_deseada):
    if cantidad_deseada > stock_actual:
        # Si se pide más de lo que hay, lanzamos un error.
        raise IndexError("No hay suficiente stock disponible para la cantidad solicitada.")
    print(f"Compra exitosa de {cantidad_deseada} unidades.")

# Uso:
try:
    comprar_producto(5, 2)
    comprar_producto(5, 7) # Esto lanzará el IndexError
except IndexError as e:
    print(f"Error de stock: {e}")



def acceder_panel_admin(rol_usuario):
    if rol_usuario != "admin":
        # Si el rol no es 'admin', no está autorizado.
        raise PermissionError("Acceso denegado: Se requieren permisos de administrador.")
    print("Acceso al panel de administrador concedido.")

# Uso:
try:
    acceder_panel_admin("editor") # Esto lanzará el PermissionError
    acceder_panel_admin("admin")
except PermissionError as e:
    print(f"Error de autorización: {e}")

print()
print()
def procesar_numero(dato_str):
    try:
        num = int(dato_str) # Podría dar ValueError
        return num * 10
    except ValueError as e:
        print(f"DEBUG: Error local en procesar_numero: '{dato_str}' no es un número.")
        raise e # Re-lanza el mismo ValueError para que lo atrape 'main'

def main_app():
    try:
        resultado = procesar_numero("XYZ") # Esto llamará a procesar_numero y fallará
        print(f"Resultado: {resultado}")
    except ValueError as e_general:
        print(f"ERROR GLOBAL: No se pudo procesar el dato. Detalle: {e_general}")

# Uso:
main_app()



print()
print()
def cargar_configuracion(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as f:
            contenido = f.read()
        return contenido
    except FileNotFoundError as e:
        print(f"ADVERTENCIA: No se encontró el archivo '{ruta_archivo}'. Reintentando o fallando.")
        raise e # Re-lanzamos para que la aplicación principal sepa del problema

def iniciar_servidor():
    try:
        config = cargar_configuracion("config.txt") # Intentamos cargar un archivo
        print("Servidor iniciado con configuración:", config)
    except FileNotFoundError as e_final:
        print(f"ERROR CRÍTICO: No se pudo iniciar el servidor sin configuración. {e_final}")
        exit() # Detenemos el programa si la configuración es esencial

# Uso:
iniciar_servidor() # Si 'config.txt' no existe, verás la ADVERTENCIA y luego el ERROR CRÍTICO



print()
print()

import re # Módulo para expresiones regulares

def validar_email_interno(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        # Si el formato no es válido, lanzamos un ValueError
        raise ValueError(f"Formato de correo inválido: {email}")
    print(f"Email '{email}' validado internamente.")

def registrar_usuario(email, password):
    try:
        validar_email_interno(email) # Podría lanzar un ValueError
        print(f"Usuario {email} y contraseña registrados.")
    except ValueError as e:
        print(f"PROBLEMA: La validación interna falló para {email}.")
        raise e # Re-lanza el ValueError para que lo capture la interfaz de usuario

# Uso:
try:
    registrar_usuario("usuario@ejemplo.com", "pass123")
    registrar_usuario("correo_invalido", "pass456") # Esto fallará
except ValueError as e_ui:
    print(f"MENSAJE AL USUARIO: No se pudo registrar. {e_ui}")

    print()
    print()

def ask_for_user_information():
    try:
        age = int(input('Ingrese su edad: ')) # Puede fallar con ValueError si no es número
        if age < 1 or age > 100:
            # Si la edad no está en el rango que queremos, ¡lanzamos un ValueError!
            raise ValueError("La edad debe estar entre 1 y 100.")

    except ValueError as ex: # Atrapamos el ValueError (ya sea de int() o el que lanzamos nosotros)
        print(f"Ingrese una edad válida! Detalle: {ex}")
        raise ex # ¡Re-lanzamos la excepción!

def main():
    try:
        ask_for_user_information() # Esta función podría lanzar una excepción
        #create_order() # Si no hay errores, se podría continuar aquí
    except Exception as ex: # El 'except' general que atrapa cualquier cosa que se re-lance
        print(f"Un error general ocurrió en la aplicación: {ex}")
        exit() # Termina el programa de forma controlada

if __name__ == '__main__':
    main()