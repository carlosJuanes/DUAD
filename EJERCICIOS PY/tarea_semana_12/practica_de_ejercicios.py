"""TEMA DE HERENCIA"""
print("-------------------------------------------------------------")
print("HERENCIA")
"""CLASE PADRE"""


class Vehiculo:
    def __init__(self, color):
        self.color = color
        print(f"Creando un Vehículo de color {self.color}")

    def arrancar(self):
        print("El vehículo ha arrancado.")


"""CLASE HIJA"""
class Coche(Vehiculo):
    def __init__(self, color, marca):
        # Llama al constructor de la clase padre (Vehiculo)
        super().__init__(color) 
        self.marca = marca
        print(f"Creando un Coche de marca {self.marca}")

    def pitar(self):
        print("¡Honk, honk!")


"""CREANDO UN OBJETO Y USANDO LOS METODOS HEREDADOS"""
mi_coche = Coche("rojo", "Toyota")

# Usando un método heredado de Vehiculo
mi_coche.arrancar()

# Usando un método propio de Coche
mi_coche.pitar()

# Accediendo a atributos de la clase padre y la clase hija
print(f"Mi coche es de color {mi_coche.color} y es un {mi_coche.marca}.")

"""Resumen
Con constructor propio: Se usa super().__init__() para inicializar los atributos del padre y luego los propios.

Sin constructor propio: El constructor del padre se hereda y se usa directamente."""



print("--------------------------------------------------------------------")
"""TEMA DE HERENCIA MULTPLE"""
print("HERENCIA MULTIPLE")
"""CLASE PADRE COCHE"""
class Coche:
    def mover(self):
        print("El coche se mueve por tierra.")

"""CLASE PADRE BARCO"""
class Barco:
    def mover(self):
        print("El barco se mueve por agua.")

"""CLASE HIJA"""
class CocheAnfibio(Coche, Barco):
    pass # No tiene atributos ni metodos propios, hereda de sus padres

"""CREANDO OBJETOS"""
mi_vehiculo = CocheAnfibio()
mi_vehiculo.mover()



print("--------------------------------------------------------------------")
"""TEMA DE ENCAPSULAMIENTO"""
print("ENCAPSULAMIENTO")
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        # El guion bajo indica que este atributo es "protegido"
        self._saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito de {cantidad} realizado.")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0 and self._saldo >= cantidad:
            self._saldo -= cantidad
            print(f"Retiro de {cantidad} realizado.")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def consultar_saldo(self):
        return self._saldo
    
mi_cuenta = CuentaBancaria(500)

# Correcto: Usar los métodos para depositar y retirar
mi_cuenta.depositar(200)
mi_cuenta.retirar(100)

print(f"Saldo actual: {mi_cuenta.consultar_saldo()}")

# INCORRECTO: Acceso directo al atributo (no recomendado)
# Aunque Python lo permite, es una mala práctica
mi_cuenta._saldo = 1000000 

print(f"Saldo despues de acceso directo: {mi_cuenta.consultar_saldo()}")






print("--------------------------------------------------------------------")
"""TEMA DE ENCAPSULAMIENTO"""
print("GETTERS AND SETTERS")
class Coche:
    def __init__(self, velocidad_inicial):
        self._velocidad = velocidad_inicial

    @property
    def velocidad(self):
        print("Obteniendo la velocidad...")
        return self._velocidad

    @velocidad.setter
    def velocidad(self, nueva_velocidad):
        if nueva_velocidad >= 0:
            print("Estableciendo la nueva velocidad...")
            self._velocidad = nueva_velocidad
        else:
            raise ValueError("La velocidad no puede ser negativa.")

# Creando una instancia
mi_coche = Coche(60)

# Usando el getter (accedemos como si fuera un atributo)
print(mi_coche.velocidad)  # La salida es: Obteniendo la velocidad... 60

# Usando el setter (lo usamos para cambiar el valor)
mi_coche.velocidad = 80  # La salida es: Estableciendo la nueva velocidad...
print(mi_coche.velocidad)  # La salida es: Obteniendo la velocidad... 80

# Intentando asignar un valor inválido
try:
    mi_coche.velocidad = -10
except ValueError as e:
    print(e) # La salida es: La velocidad no puede ser negativa.

"""
- `public ()`: pueden ser accesados desde cualquier lugar.
- `protected (-)`: pueden ser accesados desde los métodos de la clase y sus clases hijas.
- `private(--)`: pueden ser accesados solo desde los métodos de la clase."""