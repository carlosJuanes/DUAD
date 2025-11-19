#------ENTRADA DE DATOS----
#pedimos al usuario que ingrese las horas trabajadas
#usamos float () para asegurarnos que el numero pueda tener decimales
horas_trabajadas=float(input("ingrese las horas trabajadas"))

#pedimos al usuario que ingrese la tarifa por horas
tarifa_por_horas=float(input("ingrese la tarifa por horas:"))

#PROCESAMIENTO DE DATOS
#calculamos el salario multiplicando horas por tarifa
salario_calculado=horas_trabajadas*tarifa_por_horas

#SALIDA DE DATOS 
#mostramos el resultado de una manera clara
print (f"la persona trabajo{horas_trabajadas} horas a una tarifa de {tarifa_por_horas}por hora")
print (f"por lo tanto, su salario es de {salario_calculado:.2f}")
