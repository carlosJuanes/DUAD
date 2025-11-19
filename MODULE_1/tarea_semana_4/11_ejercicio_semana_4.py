#11 Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, ingresando 1 si es mujer o 2 si es hombre, 
# y muestre al final el porcentaje de mujeres y hombres.


cantidad_de_personas=6
contador=1
mujeres=0
hombres=0
porcentaje_de_mujeres=0
porcentaje_de_hombres=0

while contador<=cantidad_de_personas:
    sexo_de_las_personas=int(input(f"ingrese el sexo de la persona numero {contador}. ingrese 1 si es mujer 2 si es hombre"))
    if sexo_de_las_personas==1:
        mujeres=mujeres + 1
    elif sexo_de_las_personas==2:
        hombres=hombres+1
    contador=contador+1

porcentaje_de_mujeres=mujeres*100/cantidad_de_personas
porcentaje_de_hombres=hombres*100/cantidad_de_personas

print(f"el porcentaje de mujeres es de {porcentaje_de_mujeres}%")
print(f"el porcentaje de hombres es de {porcentaje_de_hombres}%")
