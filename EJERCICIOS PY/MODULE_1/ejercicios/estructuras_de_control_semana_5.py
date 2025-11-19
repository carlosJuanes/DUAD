my_number=4
if(my_number<7):
    print(f"{my_number} es menor a 7")
else:
    print("la condicion es falsa")    


my_number=9
if(my_number<7):
    print(f"{my_number} es menor a 7")
else:
    print("la condicion es falsa")

if(2<1):
    print("esto va dentro de la condicio")
    print("esto tambien")
print("esto va fuera de la condicion")


if (2>1):
    print("esto va dentro de la condicio")
    print ("esto tambien")
print("esto va fuera de la condicio")


my_number=3
if(my_number==1):
    print("es uno")
elif(my_number==2):
    print("es dos")
elif(my_number==3):
    print("es tres")
else:
    print("no es 1, ni 2, ni 3")


counter=1
while(counter<5):
    print(f"el contador va por {counter}")
    counter+=1
print("el while ha terminado")
    

list_of_dirty_dishes=[
    1,
    2,
    3,
]
for dirty_dish in list_of_dirty_dishes:
    print(f"lavando plato numero {dirty_dish}")
print("lavado completo")


list_of_cars_brands=[
    "merdeces",
    "toyots",
    "honda",
    "mazda"
]

for brands_cars in list_of_cars_brands:
    print(f"ejecutando el ciclo para marca: {brands_cars}")
print("ciclo completado")
