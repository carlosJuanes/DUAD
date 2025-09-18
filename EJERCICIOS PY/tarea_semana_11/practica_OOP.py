print("//////////////////////////////")
print("-----CLASE-------")
class Carro:
    def __init__(self, color, marca):
        self.color=color
        self.marca=marca

mi_carro=Carro("rojo", "honda")
tu_carro=Carro("azul", "toyota")
print(f"mi carro es color: {mi_carro.color} y marca: {mi_carro.marca}")
print(f"tu carro es color: {tu_carro.color} y marca: {tu_carro.marca}")
print()
print("//////////////////////////////")
print("------ATRIBUTOS DE INSTANCIA-----")
class Carro:
    # Atributo de clase: es el mismo para todos los Carro
    ruedas = 4

    def __init__(self, color, marca):
        # Atributos de instancia: son únicos para cada objeto
        self.color = color
        self.marca = marca

# Creando dos objetos
mi_carro = Carro("rojo", "honda")
tu_carro = Carro("azul", "toyota")

# Accediendo a un atributo de instancia (valores diferentes)
print(mi_carro.color)
print(tu_carro.color)

# Accediendo al atributo de clase (mismo valor para ambos)
print(mi_carro.ruedas)
print(tu_carro.ruedas)

print()
print("//////////////////////////////")
print("------EJERCICIO DE FOTOGRAFIA-----")

class PhotographyCamera:
	photographies = []

	def __init__(self, storage_size_in_mb):
		# each photo takes around 10mb
		self.max_photographies = storage_size_in_mb / 10
	
	def take_photo(self, photography):
		if len(self.photographies) >= self.max_photographies:
			print("My storage is full!")
			return

		self.photographies.append(photography)
		
kodak_camera = PhotographyCamera(50)
kodak_camera.take_photo("My car")
kodak_camera.take_photo("My house")
print(kodak_camera.photographies)

print()
print("//////////////////////////////")
print("-------HERENCIA-----")
# Esta es la clase padre o superclase
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print(f"{self.nombre} está comiendo.")

# Esta es la clase hija o subclase que hereda de Animal
class Perro(Animal):  # Aquí se define la herencia
    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

# Creamos un objeto de la clase Perro
mi_perro = Perro("Fido", 3)

# El objeto Perro puede usar los métodos de su clase padre (Animal)
mi_perro.comer()

# Y también puede usar sus propios métodos
mi_perro.ladrar()

print()
print("////////////////////////////////////")
print("-------SELF COMO NOMBRE DEL OBJETO------")
class Car:
	wheel_number = 4
	gas_type = "diesel"
	
	def my_first_method(self):
		print("Hello OOP World!")

	def show_history(self, miles, crashes):
		print(f"This car has {miles} miles, {crashes} crashes and {self.wheel_number} wheels")
		
	def upgrade_engine(self):
		if self.gas_type == "diesel":
			print("Cambiando el motor diesel por uno de gasolina super por $2000...")
			self.gas_type = "super"
		else:
			print("Este automovil ya tiene un motor de gasolina super!")



print("Primer auto")
my_car_1 = Car()
print("Auto fabricado")
print(my_car_1.gas_type)

my_car_1.upgrade_engine()

print("Auto mejorado")
print(my_car_1.gas_type)


my_car_1.upgrade_engine()

print("Segundo auto")
my_car_2 = Car()
print(my_car_2.gas_type)



print()
print("//////////////////////////////")
print("-------EJEMPLO DE CAMARA FOTOGRAFICA------")
class PhotographyCamera:
	photographies = []

	def __init__(self, storage_size_in_mb):
		# each photo takes around 10mb
		self.max_photographies = storage_size_in_mb / 10
	
	def take_photo(self, photography):
		if len(self.photographies) >= self.max_photographies:
			print("My storage is full!")
			return

		self.photographies.append(photography)
		
kodak_camera = PhotographyCamera(50)
kodak_camera.take_photo("My car")
kodak_camera.take_photo("My house")
print(kodak_camera.photographies)


print()
print("////////////////////////////////////")
print("-------EJERCICIOS DE PRACTICA------")
print()
print("-------------------------------------")
print("------------EJERCICIO N1-------------")
print("-------------------------------------")
"""EJERCICIO OOP
Instrucciones:
1. Creación de la Clase:
Crea una clase llamada Libro.
Esta clase debe tener un método constructor __init__ que inicialice los siguientes atributos de instancia: titulo, autor, y paginas.
2. Atributo Adicional:
Dentro del constructor, agrega un nuevo atributo de instancia llamado paginas_leidas y asígnale un valor inicial de 0. Este atributo no debe ser un parámetro del constructor.
3. Métodos:
Crea un método llamado leer_paginas que acepte un parámetro cantidad. Este método debe sumar la cantidad a paginas_leidas.
Agrega lógica al método leer_paginas para que el paginas_leidas no exceda el número total de paginas del libro.
Crea un método llamado obtener_progreso que calcule y retorne el porcentaje de páginas leídas.
Crea un método llamado terminar_libro que retorne True si el libro está completamente leído (paginas_leidas es igual a paginas) y False en caso contrario. Además, debe imprimir un mensaje apropiado en cada caso.
4. Implementación y Pruebas:
Crea una instancia de la clase Libro con los datos de tu libro favorito.
Llama al método leer_paginas varias veces con distintos valores.
Llama al método terminar_libro para verificar el estado del libro.
Prueba que la lógica para no exceder las páginas del libro funcione correctamente.
"""
class Libro:
	def __init__(self, titulo, autor, paginas):
		self.titulo=titulo
		self.autor=autor
		self.paginas=paginas
		self.paginas_leidas=0

	
	def obtener_progreso(self):
		porcentaje=self.paginas_leidas/self.paginas*100
		return porcentaje

	def leer_paginas(self, leidas):
		if (self.paginas_leidas+leidas)<=self.paginas:
			self.paginas_leidas+=leidas
			print(f"Se han leido {self.paginas_leidas} paginas en total.")
			print(f"has leido el {self.obtener_progreso():.2F}% del libro")
		else:
			x=self.paginas-self.paginas_leidas
			print(f"No puedes leer más páginas de las que tiene el libro. Te faltan {x} páginas.")
	
	def mostrar_informacion(self):
		print(f"El libro {self.titulo} fue escrito por {self.autor} y tiene {self.paginas} paginas")


	def terminar_libro(self):
		if self.paginas_leidas==self.paginas:
			print(" Felicidades acaba de terminar de leer el libro!!!")
			return True
		else:
			restantes=self.paginas-self.paginas_leidas
			print(f"No te rindas aun faltan {restantes} paginas para terminar el libro")
			return False
		

my_Libro=Libro("carlos","afredo",500)
my_Libro.mostrar_informacion()
my_Libro.leer_paginas(40)
progreso_actual=my_Libro.obtener_progreso()
print(f" el progreso actual de lectura es de {progreso_actual}")
libro_terminado=my_Libro.terminar_libro()
if libro_terminado:
	print("Felicidades acaba de terminar de leer el libro")
else:
	print("No se rinda ya falta poco para terminar de leer el libro")


print("-------------------------------------")
print("------------EJERCICIO N2-------------")
print("-------------------------------------")

"""Creación de la cuenta: El constructor __init__ debe recibir y almacenar el nombre del titular y el saldo inicial.
Adicionalmente, debe inicializar una lista vacía para las transacciones.

Depósitos: Implementa un método depositar que acepte un monto. 
Este método debe sumar el monto al saldo, agregar la transacción a la lista y confirmar la operación con un mensaje.

Retiros: Implementa un método retirar que acepte un monto. Si el monto es mayor que el saldo,
debe mostrar un mensaje de error y no realizar la transacción. Si es válido, debe restarlo del saldo, 
agregar la transacción (como valor negativo) a la lista y confirmar la operación.

Consulta de saldo: El método obtener_saldo debe devolver el saldo actual de la cuenta.

Historial: El método mostrar_historial debe imprimir todas las transacciones de la lista.
Una vez que la clase esté completa, crea una instancia y prueba sus métodos con una serie de depósitos, 
retiros exitosos y fallidos, y consultas de saldo e historial
para demostrar que tu código responde a todos los requerimientos."""

class CuentaBancaria:
	def __init__(self, nombre, saldo):
		self.transacciones=[]
		self.nombre=nombre
		self.saldo=saldo

	def deposito(self,monto):
		self.saldo+=monto
		self.transacciones.append(monto)
		print(f"Se ha realizado un deposito de {monto}, su nuevo saldo es de {self.saldo}")

	def retiro(self, monto):
		if self.saldo>=monto:
			self.saldo-=monto
			print(f"su retiro de {monto} se realizo exitosamente!!!")
			print(f"su saldo actual es: {self.saldo}")
			self.transacciones.append(-monto)
		else:
			print("Error fondos insuficientes, pruebe con otra cantidad")

	def obtener_saldo(self):
		return self.saldo
	
	def imprimir_historial(self):
		print("------HISTORIAL DE TRANSACCIONES------")
		for line in self.transacciones:
			print(f"{line}")
		print("--------------------------------------")


my_cuenta=CuentaBancaria("carlos",0)
my_cuenta.deposito(100)
my_cuenta.deposito(100)
my_cuenta.deposito(800)
my_cuenta.imprimir_historial()
my_cuenta.retiro(200)
my_cuenta.retiro(600)
my_cuenta.retiro(50)
my_cuenta.retiro(50)
saldo_actual=my_cuenta.obtener_saldo()
print(f"Su saldo actual es de: {saldo_actual} impreso desde una variable")
my_cuenta.imprimir_historial()
