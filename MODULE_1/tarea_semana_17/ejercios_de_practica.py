# import FreeSimpleGUI as sg

# counter = 0

# # Declarar los elementos
# layout = [
#     [sg.Text("Haz click en lo que quieras hacer")],
#     [sg.Text(counter, key="-COUNTER-")],
#     [sg.Button("Sumar"), sg.Button("Restar")],
# ]

# # Crear la ventana
# window = sg.Window("Primer programa", layout)

# # Event Loop para procesar "events" y obtener los "values" de los inputs
# while True:
#     event, values = window.read()
#     # Procesar el evento del cerrar la ventaja
#     # (si el usuario lo hace)
#     if event == sg.WIN_CLOSED:
#         break
#     elif event == "Sumar":
#         counter += 1
#     elif event == "Restar":
#         counter -= 1

#     window["-COUNTER-"].update(counter)

# window.close()


# print("/////////////////////////////////////////////////////")
# print("/////////////////////////////////////////////////////")
# print("/////////////////////////////////////////////////////")
# #1-  Create a program that allows me to enter information for 'n' video games and save it to a text file.


# import csv

# header=["name", "genre", "developer", "classification"]
# def enter_video_games():
#     video_games=[]
#     while True:
#         entered_video_games=input("Do you want to enter video games into the database? ")
#         video_games_lowercase=entered_video_games.lower()
#         if video_games_lowercase=="yes":
#             name=input("Enter the name of the video game: ")
#             genre=input("Enter the genre of the video game: ")
#             developer=input("Enter the developer of the video game: ")
#             classification=input("Enter the classification of the video game: ")
#             current_video_game={
#                 "name":name,
#                 "genre":genre,
#                 "developer":developer,
#                 "classification":classification
#             }
#             video_games.append(current_video_game)
#         elif video_games_lowercase=="no":
#             break
#         else:
#             print("Invalid response. Please enter yes or no.")
#     return video_games


# def save_video_games(file_path, data, header):
#     with open(file_path, "w",encoding="utf-8", newline="") as file:
#         writer=csv.DictWriter(file,fieldnames=header)
#         writer.writeheader()
#         writer.writerows(data)


# my_games=enter_video_games()
# save_video_games("videojuegos.csv",my_games,header)



# print("/////////////////////////////////////////////////////")
# print("/////////////////////////////////////////////////////")
# print("/////////////////////////////////////////////////////")
# 3-. Create a program that opens a .csv file with video game information (the one generated in exercise 1) and:
# - Reads each line using `csv.reader()`
# - Displays the content on screen in a readable format, line by line
# import csv
# def file_reader(path):
#     with open(path, "r", newline='') as file:
#         reader=csv.reader(file)
#         headers=next(reader)
#         for row in reader:
#             for key, value in zip(headers, row):
#                 print(f"{key}:{value}")
#             print()

# file_reader("videojuegos.csv")





# """3. Create an object structure that resembles a Binary Tree.
#     1. It must include a method to print the entire structure.
#     2. The use of composite data types such as `lists`, `dicts`, or `tuples`, or modules like `collections` is not allowed."""

# class Node: #creamos un node, es node tendra un data y tendra una derecha y una izquierda
#     def __init__(self, data):
#         self.data=data  #cada derecha e izquierda tendra un node en si mediante se valla llenando
#         self.left=None
#         self.right=None

# class BinaryTree: #declaramos la clase la cual tendra el root la raiz bacia, a que corresponde la raiz es un node el cual ira teniendi dertecha y izquierda?
#     def __init__(self):
#         self.root=None

#     def insert(self, root, new_data):
#         if root is None: #en este metodo llenamos los nodes en este caso verificamos si esta vacio
#             return Node(new_data)  #si esta vacio creamos el node con la dara que recibamos del metodo insert
        
#         if new_data< root.data: #si no esta vacio lo iremos llendo y es aqui donde me surgen dudas.
#             root.left= self.insert(root.left, new_data) #verificamos si el data es menor al data de root  de ser asi lo iremos agregando a la izquierda de el node
#             pero para eso navegamos hacia ahi vamos hacia el root.left y ahi usamos la funcion que estamos creando
#             "insert(self, root, new_data)"  aqui usamos el root.left y le damos la nueva data ya que esta funcion sirve para agregar al rut que estemos declarando como parametro 
#         else:
#             root.right=self.insert(root.right, new_data) # si en new data es mayor lo agregaremos a la derecha
#             navegamos hacia el root.right  y llamamos la funcion que estamos creando, y como 
#             parametros usamos el root.right que estams modificando eso asumo que sera 0? y a la par el new data
#             al final que estamos haciendo estamos agregando el root  al arbol o que representa cada root mejor dicho representa un node?
#             hasta ahora analizo hasta aqui asi que comentame hasta aqui despues cuando tenga clara esta parte 
#             pasare a la siguiente parte del print por los momentos dime si mi entendimiento es correcto 
#             solo corrigeme despues de la correccion me daras tu analisis parte por parte de esta parte solo hasta aqui ya que
#             despues iremos por el resto del codigo
#         return root
#     def print(self, node):
#         if node is not None:
#             self.print(node.left)
#             print(node.data, end=" ")
#             self.print(node.right)



# tree_root = None # crea una  variable vacia que contendra la lista de los valores de los nodes es decir
# aqui se ira construyendo el arbol?
# datos = [50, 30, 70, 20, 40, 60, 80] # aqui tiene los nodes que necesitaremos ordenar e imprimir
# tree=BinaryTree()# hace la instancia de la clase para poder usar sus metodos o funciones
# print("--- CONSTRUYENDO EL ÁRBOL ---")

# for dato in datos: #itera en la lista des ordenada dato  por dato
#     tree_root = tree.insert(tree_root, dato)# aqui va agregando los  valores ordenandolos 
#     de acuerdo a su valor izquierda o derecha construyendo el arbol
#     print(f"Insertando: {dato}")

# print("\n--- IMPRESIÓN COMPLETA (IN-ORDER) ---")
# tree.print(tree_root)# en este caso hace uso de el metodo print de la clase es aqui donde se vera la lista ordenada e impresa
# print("\n-------------------------------------")
# print("\n-------------------------------------")
# print("\n-------------------------------------")
# print("\n-------------------------------------")



# """4 - Create an object structure that represents a basic queue (Queue) with linked objects."""

# creamos la clase  node el cual tendra data y el next que se inicializa vacio para ir
# agregando datos conforme avance 
# class Node:
#     data: str #se espera string
#     next: "Node" # se espéra que el next sea un node 
    
#     def __init__(self, data, next=None):
#         self.data=data
#         self.next=next

# se crea la clase queue que es una fila de primeras entradas primeras salidas
# se crea para usar sus entradas salidas y para imprimir osea sus metodos 
# class Queue:
#     head: Node # se inicializa con el node como head

#     def __init__(self):
#         self.head=None

#     def enqueue(self, data): #aqui agregaremos datos como nodos 
#         new_node=Node(data)# declaramos la variable new node creando una instacia de la clase node
#         if self.head is None:#en este caso validamos si esta vacia la fila sin nodes o datos
#             self.head=new_node# de estar vacia el new node sera su primer dato agregado
#             return# aqui asumo que usamos el return para salir
#         current_node=self.head# si no esta vacio identificamos el head para empezar a movernos desde ahi
#         while current_node.next is not None:#verificamos que mientras el current node. next  que es de donde partimos no este vacio 
#             current_node=current_node.next#pasaremos el current node al next lo que nos permitira llegar hasta el ultimo node de la lista
#         current_node.next=new_node#una vez encontramos el ultimo node pasamos a actualizar el current node . next con el calor del nuevo node que queremos agregar al final de la lista

#     def dequeue(self):#aqui quitaremos nodes en este caso del inicio de la fila 
#         if self.head is None:#verificamos si la fila esta vacia y de ser asi la retornamos vacia none
#             return None
#         remove_data=self.head.data#si no esta vacia creamos una variable solo para poder almacenar el data de ese node a eliminar
#         self.head=self.head.next# cambiamos el apuntador del head a su next para poder eliminar el primer node
#         print(f'"{remove_data}"')# imprimimos la variable que almacena el data del node eliminado
#         return remove_data#retornamos el data del node eliminado para que se vea en la salida como impreso
    
#     def print_all(self):#imprimiremos los valores que se encuentren en la lista en el momento de llamar este metodod e la clase 
#         current_node=self.head#partimos declarando el current con el node head para empezar desde ahi la impresion
#         output=" "# este espacio lo usamos para fines de imprecion en pantalla para que cumpla con lo que el ejercicio requiere
#         while current_node is not None: #validamos que estemos iterando sobre los nodos con informacion
#             output+=str(current_node.data)#agregamos la data del current actual a output que haviamos creado con el espacio vacio
#             current_node=current_node.next#movemos el apuntador del current a su next
#             if current_node is not None:#verificamos que no sea el current un node vacio para seguir agregando esos espacios y simbolos para fines de impresion
#                 output+=" -> "
#         print(output)# al final imprimimos  los valores recaudados en el output con los simbolos para fines de impresion

# q=Queue()
# print("_____ADDING DATA_____")
# q.enqueue("A")
# q.enqueue("B")
# q.enqueue("C")
# q.enqueue("D")
# q.enqueue("E")
# q.enqueue("F")
# q.print_all()
# print("_____DELETING DATA_____")
# q.dequeue()
# q.dequeue()
# print("_____FINAL PRINT_____")
# q.print_all()








# """6. Doubly Linked List
# - Requirements:
# - Each node must have a reference to the next and to the previous node
# - Methods:
# append(data): Adds to the end
# prepend(data): Adds to the beginning
# delete(data): Removes the first node with that value
# print_forward() and print_backward(): Prints in both directions"""


# class Node:
#     data:str
#     next:"Node"
#     before:"Node"
#     def __init__(self, data, before=None, next=None):
#         self.data=data
#         self.next=next
#         self.before=before
        
# class DoublyLinkedList:
#     head=Node
#     def __init__(self):
#         self.head=None
#         self.tail=None

#     def append(self, data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#             self.tail=new_node
#             return
#         else:   
#             new_node.before=self.tail
#             self.tail.next=new_node
#             self.tail=new_node
    
#     def prepend(self, data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#             self.tail=new_node
#             return
#         else:
#             new_node.next=self.head
#             self.head.before=new_node
#             self.head=new_node

#     def delete(self, data):
#         current_node=self.head
#         previous_node=None

#         if current_node is None:
#             return False
        
#         if current_node.data==data:
#             self.head=current_node.next
#             if self.head is not None:
#                 self.head.before=None
#             else:
#                 self.tail=None
#                 return True
            
#         while current_node is not None and current_node.data!=data:  #verificamos que no sea los dos casos anteriores
#             previous_node=current_node#movemos o guardamos el valor del current en previus
#             current_node=current_node.next#ahora movemos el current al siguiente hasta encontrar cualquier de las dosc condiciones uno encontrar el data buscado y que no lo encontramos
#         if current_node is not None:# validamos el caso de no haberlo encontrado, #en caso de encontrarlo hacemos lo siguiente que esta dentro de la condicion o si no se lansa el retunr false diciendo que ninnguno de los tres casos encontraron el dato por lo que el delete no se ejecutara
#             previous_node.next=current_node.next# el previus tiene el valor anterir por lo quue usamos su next para conectarlo con el next del current actual para que de esa manera se elimine el dato  buscado que contendra el current
#             if current_node.next is not None:# valiadmos que si el current next que sera elnuevo current no este vaio esto valida si estamos eliminado el ultmo del recorrido
#                 current_node.next.before=previous_node#si no es el ultimo solo le agregamos a su before el valor del previus ya de esa manera lo conectamos omitiendo el valor del que buscamos
#             else:
#                 self.tail=previous_node#y si el que eliminamos era el ultimo simplemente apuntamos el tail al previus que es el que quedo de ultimo
#             return True #retornamos que si se elimino
#         return False#si apesar de todos los escenarios no se encontro retornamos false no se logro eliminar
    
#     def print_forward(self):
#         current_node=self.head
#         output=""
#         while (current_node is not None):#validamos que mientras el current que se ira mivuendo no sea none hacemos lo siguiente
#             output+=str(current_node.data)#vamos añadiendo a la variable vacia el data en modo de str
#             current_node=current_node.next#vamos moviendo el current  al siguiente para ir avanzando hasta encontranos cn el none
#             if current_node is not None:#mientras no encontremos el none
#                 output+= " -> "#vamos a ir imprimiendo eso dentro de la variable que ira almacenando los valores str con esos simbolos para fines de impresion
#         print(output)#por ultimo imprimimos la variabe con todos los datos de izquierda a derecha

#     def print_backward(self):#estees lo mismo que el anterior solo que de derecha a izquiera
#         current_node=self.tail
#         output=""
#         while (current_node is not None):
#             output+=str(current_node.data)
#             current_node=current_node.before
#             if current_node is not None:
#                 output+= " -> "
#         print(output)

# dll=DoublyLinkedList()#declaramos la clase para poder usar sus metodos o funciones
# dll.append("A")#agregamos al inicio ya que sera el primer valor
# dll.append("B")#agregamos al final a la derecha 
# dll.append("C")#seguimos agregando a la derecha 
# dll.print_forward()#imprimimos de izquierda a derecha
# dll.print_backward()#ahora de derecha a izquierda
# dll.delete("B")#borramos el b en este caso tuvimos que pasar de " while current_node is not None and current_node.data!=data" por esta  condicion para poder encontrarlo al centro
# dll.print_forward()
# dll.print_backward()


# "//////////////////////////////////////////////////////////"
# "//////////////////////////////////////////////////////////"
# "//////////////////////////////////////////////////////////"
# "//////////////////////////////////////////////////////////"


# """1- Create a bubble sort on your own without reviewing the lesson's code."""

# def my_bubble_sort(list_to_sort):#empezaremos con una lista de datos o numeros en esta caso es lo que recibiremos
#     for outer_index in range(0, len(list_to_sort) -1):#iteramos de manera externa desde 0 hasta el tamaño de la lista menos 1 lo cual el primer index sera 0
#         has_made_change= False#empezamos asumiendo que no hubo cambios 
#         for index in range(0, len(list_to_sort)-1 -outer_index):#iteramos de manera interna desde 0 hasta el tamaño de la lista menos 1, en esta primera iteracion estamos omitiendo el valor del externo que seria 0 quedaria 0, 5-1-0=4
#             current_element=list_to_sort[index]#el primer elemento sera el index 0 en este caso sera 1
#             next_element=list_to_sort[index+1]# el valor del next sera 0+1 que sera dentro de la lista el 2
#             print(f"iterating: {outer_index} - {index}, current element: {current_element}, next element: {next_element}")
#             imprimimos el outer que sera 0 y el index que tambien sera 0 el current sera  1 y el next sera el 2
#             if current_element>next_element: #verificamos para mover pero en este ejemplo no se mueve nada
#                 print(f"the current number is greater than the next number, moving...")
#                 list_to_sort[index]=next_element
#                 list_to_sort[index+1]=current_element
#                 has_made_change=True
#         if not has_made_change:
#             return list_to_sort
#     return list_to_sort

# my_list=[1, 5, 7, 4, 2]
# my_bubble_sort(my_list)
# print(my_list)


# print ("//////////////////////////////////////////////////")

# def my_bubble_sort(list_to_sort):
#     N = len(list_to_sort)
#     print(f"--- Lista Inicial: {list_to_sort} ---")
    
#     BUCLE EXTERNO: Define cuántos elementos están fijos a la izquierda (ordenados)
#     for outer_index in range(0, N - 1):
#         has_made_change = False
        
#         El punto de parada es outer_index - 1
#         print(f"\n[PASADA EXTERNA {outer_index + 1}] outer_index: {outer_index}. Frontera de orden: {outer_index}")
        
#         BUCLE INTERNO: Recorre de derecha a izquierda (desde el último índice hasta la frontera)
#         for index in range(N - 1, outer_index - 1, -1):
            
#             current_element (a la derecha) necesita un elemento a su izquierda (index - 1)
#             El bucle debe parar antes de index=0, que es la frontera
#             if index == 0:
#                 continue # Evita error al intentar acceder a [index - 1] cuando index es 0
            
#             current_element = list_to_sort[index]
#             before_element = list_to_sort[index - 1]
            
#             print(f"  > Index {index} (C:{current_element}) vs Index {index - 1} (B:{before_element}). Lista: {list_to_sort}")
            
#             Lógica de ORDENAMIENTO DESCENDENTE: Mueve el elemento más GRANDE a la izquierda.
#             if current_element > before_element:
#                 print(f"    -- ¡Intercambio! {current_element} > {before_element}. Moviendo {current_element} a la izquierda.")
                
#                 Realiza el intercambio
#                 list_to_sort[index] = before_element
#                 list_to_sort[index - 1] = current_element
#                 has_made_change = True
            
#         Parada Rápida: Si no hubo intercambios en la pasada interna, la lista está ordenada.
#         if not has_made_change:
#             print(f"\n[PARADA RÁPIDA] No hubo intercambios en la pasada {outer_index + 1}. La lista está ordenada.")
#             return list_to_sort
            
#     return list_to_sort

# my_list = [5, 2, 8, 1, 9]
# my_bubble_sort(my_list)
# print(f"\n--- Lista Ordenada Final (Descendente): {my_list} ---")



# print("//////////////////////////////////////////////////")
# print("//////////////////////////////////////////////////")
# print("//////////////////////////////////////////////////")
# print("//////////////////////////////////////////////////")
# print("//////////////////////////////////////////////////")


# """- Implement a working bubble_sort for @LinkedLists
# - Modify your implementation of `bubble_sort` so that:
# - It counts how many iterations (passes) the algorithm performs
# - It counts how many swaps were made in total"""

# class Node:
#     data:int

#     def __init__(self, data, next=None):
#         self.data=data
#         self.next=None


# class LinkedList:
#     head=Node
#     def __init__(self, head):
#         self.head=head#arranca partiend de un node como cabeza

#     def print_structure(self):
#         current_node=self.head
#         output=""
#         while(current_node is not None):#validamos que el current no sea noone ya que lo iremos moviendo partiendo de head hasta el ultimo que 
#             output+=str(current_node.data)#convertimos el data del nodo actual a str ya que nos servira para impresion de datos
#             current_node=current_node.next#aqui movemos el curren hacia su next para ir revisandolos todos e imprimiendolos
#             if current_node is not None:
#                 output+=" -> "
#         print(output)

#     def bubble_sort_steps(self):#aqui intentamos direccionar  los punteros para que lleven un orden numerico
#         head=self.head#declaramos la variable head para empezar 
#         if self.head is None:#si en el caso de que este vacio retornamos el head, para que si se supone que esta vacio?
#             return head
        
#         iterations_count = 0#declaramos las variables de conteo en este caso cuantas veces se recorrio  
#         swaps_count = 0#contamos las veces que hicimos una redireccion de punteros 

#         while True:#inicializamos el primer bucle que seria el externo, 
#             iterations_count+=1#aumentamos una primer iteracion 
#             has_made_change=False#usamos una bandera en false 
#             prev=None#asumimos que el prev es none ya que esperamos empezar desde el head
#             current=self.head#le damos una variable a head para poder usarla en el reapunte de valores
#             mi pregunta es cuantas veces o que determinara cuantas veces se ejecutar este primer bucle
#             while current and current.next is not None:#mientras la cabeza que es con el que inicializaremos y su next no esten vacios haremos lo que sigue 
#                 next_node=current.next       #damos una variable next node al next del current que para empezar sera el head y su next 
                
#                 if current.data>next_node.data:#si el current data es mayor al de el next 
#                     if prev is None:#y verificamos si el prev es none porque de serlo significa que estams empezando a redireccioanar el head 
#                         self.head=next_node#y es aqui donde ejecutamos el cambio y el head pasa a ser el next node
#                     else:
#                         prev.next=next_node#pero si el prev contiene un valor se usa su next para dirijirse a el next node omitiendo al  current para que de esa manera el prev se  se conecte al next node
#                         lo anterior valida el caso que si el node que estamos intercambiando es o no el head 
#                     current.next=next_node.next# en caso de que A sea mayor que B lo que estamos buscando es un orden de menor a mayor el .next de A ahora apuntara al .next de B, es decir el next de A ahora sera C
#                     next_node.next=current#ahora el next de B sera el curret es decir ahora sera A y se ordenaria B→A
#                     prev = next_node#ahora vamos a cambiar el valor de prev el que iniciamos como none para que sea e nex node que sera B para las siguientes iteraciones y continar comparando los nodes que siguen 
#                     swaps_count+=1#en ese caso que huvo un intercmbio agregamos un 1 para la contabilizacion de los swap
#                     has_made_change=True#activamos la bandera a true para que no salgamos del bucle y lo sigamos recorriendo
#                 tdo eso fue en caso de que el A fuese mayor a B por eso se hizo el cambio 
#                 else:#y en el caso de que no hubiese sido necesario el cambio , simplemente movemos los punteros de prev siendo current y current sendo su propio next
#                     prev=current
#                     current=current.next#para seguir avanzando al siguiente node hasta que terminemos?
#             if not has_made_change:
#                 break
#         return iterations_count, swaps_count 



# N1=Node(5)
# N2=Node(4)
# N3=Node(2)
# N4=Node(3)
# N5=Node(1)

# N1.next=N2
# N2.next=N3
# N3.next=N4
# N4.next=N5

# my_list=LinkedList(N1)
# iterations_count, swaps_count=my_list.bubble_sort_steps()

# print("ordered list:")
# my_list.print_structure()
# print(f"iterations: {iterations_count}")
# print(f"swaps: {swaps_count}")

# print("-------------------------------------------------")
# print("-------------------------------------------------")
# print("-------------------------------------------------")
# print("-------------------------------------------------")
# print("-------------------------------------------------")

# """5- Input Validation before Sorting
#         -Create a function that receives a list and validates:
#         -That all elements are numbers
#         -That it is not empty
#         -Then apply bubble_sort if the validations pass
#         -If there is an error, it must return an appropriate message"""


# def bubble_sort(input_list):
#     for outer_index in range(0, len(input_list)-1):
#         has_made_change= False
#         for index in range(0, len(input_list)-1-outer_index):
#             current_element=input_list[index]
#             next_element=input_list[index+1]
#             print(f"iterating: {outer_index} - {index}, current element: {current_element}, next element: {next_element}")
#             if current_element>next_element:
#                 print("the current number is greater than the next number, moving...")
#                 input_list[index+1]=current_element
#                 input_list[index]=next_element
#                 has_made_change=True
#         if not has_made_change:
#             return input_list
#     return input_list
# esta parte del bubble sort creo manejarla solamente es ta ordenando los valores de menor a mayor 

# def validated_bubble_sort(input_list):
#     if not input_list:#validamos si la lista de entrada esta vacia
#         return ("Error the list is empty")#retornamos el errror  entoendo si no es la manera correcta no es eso lo que estamos validando solo quiero saber si le entiendo
#     for element in input_list:#recorremos cada elemento dentro de la lista
#         if not isinstance(element,(int, float)):#validamos si alguno de los elementos no es instancia de int o float lo que seria cualquier cosa que no sea numero
#             return "Error: List contains non-numeric elements"#en caso de cumplirse la condicion arrojamos error
#     return bubble_sort(input_list)#si no hay error se valido que solo son numeros se arroja la lista ya ordenada ya que se llamo a la funcion de BS desde adentro de esta funcion de validacion


# print( validated_bubble_sort([5,4,10,51,1]))#nos dara una lista ordenada
# print(validated_bubble_sort([5,4,"Hola",51,1]))#nos data uno de los errores que dice que la lista no debe de contener valores que no sean numeros


import FreeSimpleGUI as sg

counter = 0

# Declarar los elementos
layout = [
    [sg.Text("Haz click en lo que quieras hacer")],
    [sg.Text(counter, key="-COUNTER-")],
    [sg.Button("Sumar"), sg.Button("Restar")],
]

# Crear la ventana
window = sg.Window("Primer programa", layout)

# Event Loop para procesar "events" y obtener los "values" de los inputs
while True:
    event, values = window.read()
    # Procesar el evento del cerrar la ventaja
    # (si el usuario lo hace)
    if event == sg.WIN_CLOSED:
        break
    elif event == "Sumar":
        counter += 1
    elif event == "Restar":
        counter -= 1

    window["-COUNTER-"].update(counter)

window.close()