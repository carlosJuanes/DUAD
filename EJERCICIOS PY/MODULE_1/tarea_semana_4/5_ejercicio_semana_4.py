#5. Dada `n` cantidad de notas de un estudiante, calcular:
    #1. Cuantas notas tiene aprobadas (mayor a 70).
    #2. Cuantas notas tiene desaprobadas (menor a 70).
    #3. El promedio de todas.
    #4. El promedio de las aprobadas.
    #5. El promedio de las desaprobadas.



contador=1
nota_actual=0
cantidad_notas_aprobadas=0
cantidad_de_notas_desaprobadas=0
promedio_de_notas_aprobadas=0
promedio_de_notas_desaprobadas=0
promedio_de_notas_total=0

total_de_notas=int(input(f"ingrese su cantidad de notas= "))
while contador<=total_de_notas:
    nota_actual=int(input(f"ingrese la nota numero {contador}= "))
    if nota_actual<70:
        promedio_de_notas_desaprobadas=promedio_de_notas_desaprobadas+nota_actual
        cantidad_de_notas_desaprobadas=cantidad_de_notas_desaprobadas+1
    elif nota_actual>=70:
        promedio_de_notas_aprobadas=promedio_de_notas_aprobadas+nota_actual
        cantidad_notas_aprobadas=cantidad_notas_aprobadas+1
    promedio_de_notas_total=promedio_de_notas_total+nota_actual
    contador=contador+1
promedio_de_notas_total=promedio_de_notas_total/total_de_notas 
if cantidad_notas_aprobadas>0:
    promedio_de_notas_aprobadas=promedio_de_notas_aprobadas/cantidad_notas_aprobadas
else:
    promedio_de_notas_aprobadas=0
if cantidad_de_notas_desaprobadas>0:
    promedio_de_notas_desaprobadas=promedio_de_notas_desaprobadas/cantidad_de_notas_desaprobadas
else:
    promedio_de_notas_desaprobadas=0

print(f"el estudiante aprobo {cantidad_notas_aprobadas} notas")
print(f"el estudiante desaprobo {cantidad_de_notas_desaprobadas} notas")
print(f"el promedio de notas aprobadas es de {promedio_de_notas_aprobadas:.0f}%")
print(f"el promedio de notas desaprobadas es de {promedio_de_notas_desaprobadas:.0f}%")
print(f"el promedio total de notas es de {promedio_de_notas_total:.0f}%")
