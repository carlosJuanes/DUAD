def validar_nombre():
    while True:
        nombre_ingresado=input("Porfavor ingrece el  nombre completo: ")
        nombre_limpio=nombre_ingresado.strip()

        if not nombre_limpio:
            print("El nombre no puede estar vacio")
            continue
        
        nombre_valido=True
        for caracter in nombre_limpio:
            if not caracter.isalpha() and caracter !=" ":
                nombre_valido=False
                break
        if nombre_valido:
            return nombre_limpio
        else:
            print("El nombre solo debe tener letras y espacios")
        


def validar_seccion():
    while True:
        seccion=input("Porfavor ingrese la seccion del estudiante")
        seccion_limpia=seccion.strip()
        if not seccion_limpia:
            print("La seccion no debe estar vacia")
            continue
        if len(seccion_limpia)==3:
            if seccion_limpia[0:2].isdigit() and seccion_limpia[2].isalpha():
                return seccion_limpia.upper()
            else:
                print("Formato de seccion invalida el formato debe 1A, 2B,10A, 11B, etc")
        elif len(seccion_limpia)==2:
            if seccion_limpia[0].isdigit() and seccion_limpia[1].isalpha():
                return seccion_limpia.upper()
            else:
                print("Formato de seccion invalida el formato debe 1A, 2B,10A, 11B, etc")
        else:
            print("Formato de seccion invalida el formato debe 1A, 2B,10A, 11B, etc")


def estudiante_existente(estudiantes, nombre, seccion):
    for estudiante in estudiantes:
        if estudiante["Nombre completo"]==nombre and estudiante["Seccion"]==seccion:
            return True
    return False


def ingresar_estudiante(estudiantes):
    estudiante_ingresado={}
    nombre=validar_nombre().upper()
    seccion=validar_seccion().upper()
    if estudiante_existente(estudiantes, nombre, seccion):
        print("El estudiante que intenta ingresar ya existe en nuestra base de datos")
        return
    estudiante_ingresado["Nombre completo"]=nombre
    estudiante_ingresado["Seccion"]=seccion

    materias=["Nota de Español", "Nota de Ingles", "Nota de Sociales", "Nota de Ciencias"]
    for materia in materias:
        while True:
            try:
                nota=int(input(f"Porfavor ingrese la nota de la clase de {materia}"))
                if 0<=nota<=100:
                    estudiante_ingresado[materia]=nota
                    break
                else:
                    print("Porfavor ingrese una nota valida de 0-100")
            except ValueError:
                print("Porfavor ingrese un valor valido")

    notas=[]
    notas.append(estudiante_ingresado["Nota de Español"])
    notas.append(estudiante_ingresado["Nota de Ingles"])
    notas.append(estudiante_ingresado["Nota de Sociales"])
    notas.append(estudiante_ingresado["Nota de Ciencias"])

    tamaño=len(notas)
    suma=sum(notas)
    promedio=suma/tamaño
    estudiante_ingresado["Promedio"]=promedio
    return estudiante_ingresado
     
    # while True:
    #     try:
    #         español=int(input("Porfavor ingrese la Nota de Español="))
    #         if 0<=español<=100:
    #             estudiante_ingresado["Nota de Español"]=español
    #             notas.append(español)
    #             break
    #         else:
    #             print("porfavor ingrese una nota valida de 0-100")
    #     except ValueError:
    #         print("Porfavor ingrese un valor valido")
    # while True:
    #     try:
    #         ingles=int(input("Porfavor ingrese la nota de ingles= "))
    #         if 0<=ingles<=100:
    #             estudiante_ingresado["Nota de Ingles"]=ingles
    #             notas.append(ingles)
    #             break
    #         else:
    #             print("Porfavor ingrese una nota valida de 0-100")
    #     except ValueError:
    #         print("Porvafor ingrese un valor valido")
    # while True:
    #     try:
    #         sociales=int(input("Porfavor ingrese la nota de sociales= "))
    #         if 0<=sociales<=100:
    #             estudiante_ingresado["Nota de Sociales"]=sociales
    #             notas.append(sociales)
    #             break
    #         else:
    #             print("Porfavor ingrese una nota valida de 0-100")
    #     except ValueError:
    #         print("Porfavor ingrese un valor valido")
    # while True:
    #     try:
    #         Ciencias=int(input("Porfavor ingrese la nota de Ciencias= "))
    #         if 0<=Ciencias<=100:
    #             estudiante_ingresado["Nota de Ciencias"]=Ciencias
    #             notas.append(Ciencias)
    #             break
    #         else:
    #             print("Por favor ingrese una nota valida de 0-100")
    #     except ValueError:
    #         print("Por favor ingrese un valor valido")
    # numero_de_notas=len(notas)
    # promedio=sum(notas)/numero_de_notas
    # estudiante_ingresado["Promedio"]=promedio
    # return estudiante_ingresado  


def mostrar_estudiantes(estudiantes):
    if estudiantes:
        print("---------------------------------")
        print("BASE DE DATOS DE ESTUDIANTES")
        print("---------------------------------")
        for i, estudiante in enumerate(estudiantes,1):
            print(f"\nEstudiante numero {i}")
            for clave, valor in estudiante.items():
                print(f"{clave}:{valor}")
    else:
        print("aun no hay informacion en nuestra base de datos, porfavor ingrese un estudiante primero")


def mostrar_los_mejores_promedios(estudiantes):
    if estudiantes:
        estudiantes.sort(key=lambda estudiante: estudiante["Promedio"], reverse=True)
        top_3_estudiantes=estudiantes[:3]
        print("---TOP TRES DEL PROMEDIO MAS ALTO---")
        for i, estudiante in enumerate(top_3_estudiantes,1):
            print(f"Puesto numero {i}")
            for key, value in estudiante.items():
                print(f"{key}: {value}")
    else:
        print("aun no hay informacion en nuestra base de datos, porfavor ingrese un estudiante primero")


def mostrar_el_promedio_total(estudiantes):
    if estudiantes:
        promedios=[estudiante["Promedio"] for estudiante in estudiantes]
        cantidad_de_promedio=len(promedios)
        suma_de_promedios=sum(promedios)
        promedio_total=suma_de_promedios/cantidad_de_promedio
        print(f"La nota promedio del total de los estudiantes es de: {promedio_total}")
    else:
        print("aun no hay informacion en nuestra base de datos, porfavor ingrese un estudiante primero")



def eliminar_estudiante(estudiantes):
    estudiante_a_eliminar=None
    nombre_alumno_eliminar=input("Porfavor ingrese el nombre del alumno a eliminar: ")
    seccion_alumno_eliminar=input("porfavor ingrese la seccion del alumno a eliminar: ")
    eliminar_estudiante_mayuscula=nombre_alumno_eliminar.upper()
    eliminar_seccion_mayuscula=seccion_alumno_eliminar.upper()
    for i, estudiante in enumerate(estudiantes):
        if estudiante["Nombre completo"]==eliminar_estudiante_mayuscula and estudiante["Seccion"]==eliminar_seccion_mayuscula:
            print(f"se ha encontrado el Estudiante {eliminar_estudiante_mayuscula} de la seccion {eliminar_seccion_mayuscula}" )
            indice_a_eliminar=i
            estudiante_a_eliminar=estudiante
            break
    if estudiante_a_eliminar is None:
        print("No se encontro el estudiante en nuestra base de datos")
    else:
        while True:
            try:
                confirmacion=int(input("Esta seguro que desea eliminarlo?, prsione 1 para si, o presione 2 para no"))
                if confirmacion==1:
                    estudiantes.pop(indice_a_eliminar)
                    print(f"Se elimino el estudiante de la base de datos de manera exitosa!!!")
                    break
                elif confirmacion==2:
                    print("Accion cancelada")
                    break
                else:
                    print("porfavor ingrese un numero valido del 1-2")
            except ValueError:
                print("ingrese un numero valido")


def mostrar_estudiante_reprobado(estudiantes):
    print("\n--- Estudiantes Reprobados ---")
    reprobados_encontrados = False
    for estudiante in estudiantes:
        notas_reprobadas={}
        if estudiante["Nota de Español"]<60:
            notas_reprobadas["Nota de Español"]=estudiante["Nota de Español"]
        if estudiante["Nota de Ingles"]<60:
            notas_reprobadas["Nota de Ingles"]=estudiante["Nota de Ingles"]
        if estudiante["Nota de Sociales"]<60:
            notas_reprobadas["Nota de Sociales"]=estudiante["Nota de Sociales"]
        if estudiante["Nota de Ciencias"]<60:
            notas_reprobadas["Nota de Ciencias"]=estudiante["Nota de Ciencias"]
        if notas_reprobadas:
            print("\n------------------------------")
            print(f"Nombre: {estudiante["Nombre completo"]}")
            print(f"seccion: {estudiante["Seccion"]}")
            print("Materias Reprobadas")
            for clave, valor in notas_reprobadas.items():
                print(f"{clave}: {valor}")
                reprobados_encontrados = True
    if not reprobados_encontrados:
        print("No se encontraron estudiantes Reprobados")



# def validar_nombre():
#     while True:
#         nombre_ingresado = input("Por favor, ingrese el nombre completo: ")
#         nombre_limpio = nombre_ingresado.strip()
#         if not nombre_limpio:
#             print("El nombre no puede estar vacío.")
#             continue
        
#         nombre_contiene_caracter_no_deseado = False
#         for caracter in nombre_limpio:
#             if caracter.isdigit() or not caracter.isalnum() and caracter != " ":
#                 nombre_contiene_caracter_no_deseado = True
#                 break
        
#         if nombre_contiene_caracter_no_deseado:
#             print("El nombre solo debe contener letras y espacios.")
#         else:
#             return nombre_limpio