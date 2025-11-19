import csv
import data
import actions


def mostrar_menu():
    print("Bienvenido a la base de datos de los estudiantes")
    print(f"que desea hacer?:\n"
          f"1- Ingresar información de n cantidad de estudiantes, uno por uno.\n"
          f"2- Ver la información de todos los estudiantes ingresados.\n"
          f"3- Ver el top 3 de los estudiantes con la mejor nota promedio.\n"
          f"4- Ver la nota promedio entre las notas de todos los estudiantes.\n"
          f"5- Exportar todos los datos actuales a un archivo CSV.\n"
          f"6- Importar los datos de un archivo CSV previamente exportado.\n"
          f"7- Eliminar estudiante por Nombre y Seccion\n"
          f"8- Mostrar Estudiantes Reprobados\n"
          f"9- Salir.")


def seleccionar_opcion():
    while True:
        try:
            opcion=int(input("por favor ingrese una opcion= "))
            if 1<=opcion<=9:
                return opcion
            else:
                print("Error seleccione una opcion valida del 1-7 ")
        except ValueError:
            print("Error! no es una opcion valida")


def run():
    estudiantes=[]
    encabezados=["Nombre completo","Seccion","Nota de Español","Nota de Ingles","Nota de Sociales","Nota de Ciencias","Promedio"]
    while True:
        print("-------------------------------------------")
        print("----- BASE DE DATOS DE LOS ESTUDIANTES-----")
        print("-------------------------------------------")
        mostrar_menu()
        opcion_Seleccionada=seleccionar_opcion()
        if opcion_Seleccionada ==1:
            while True:
                try:
                    cantidad=int(input("cuantos estudiantes desea ingresar?= "))
                    for n in range(cantidad):
                        print(f"Estudiante N{n+1}:")
                        nuevo_estudiante=actions.ingresar_estudiante(estudiantes)
                        estudiantes.append(nuevo_estudiante)
                    break
                except ValueError:
                    print("Porfavor ingrese un numero valido")
        elif opcion_Seleccionada ==2:
            actions.mostrar_estudiantes(estudiantes)
        elif opcion_Seleccionada==3:
            actions.mostrar_los_mejores_promedios(estudiantes)
        elif opcion_Seleccionada==4:
            actions.mostrar_el_promedio_total(estudiantes)
        elif opcion_Seleccionada==5:
            if estudiantes:
                data.exportar_archivo_de_estudiantes("datos_de_estudiantes.csv",estudiantes,encabezados)
                print("Se han exportado los datos de los estudiantes a un archivo CSV de manera correcta")
            else:
                print("aun no hay informacion en nuestra base de datos, porfavor ingrese un estudiante primero")
        elif opcion_Seleccionada==6:
            estudiantes=data.importar_archivo_de_estudiantes("datos_de_estudiantes.csv")
            if estudiantes:
                print("Se ha importado el archivo de manera exitosa")
                print("La lista de estudiantes importada es:")
                for i, estudiante in enumerate(estudiantes, 1):
                    print(f"Estudiante numero {i}")
                    for clave, valor in estudiante.items():
                        print(f"{clave}: {valor}")
            else:
                print("No existe un archivo a importar")
        elif opcion_Seleccionada==7:
            actions.eliminar_estudiante(estudiantes)
        elif opcion_Seleccionada==8:
            actions.mostrar_estudiante_reprobado(estudiantes)
        elif opcion_Seleccionada==9:
            print("Saliendo...")
            print("Hasta luego!!!")
            break

