claves = ["nombre", "edad", "ciudad"]
valores = ["Carlos", 28, "Bogotá"]

mi_diccionario = {}
longitud_listas = len(claves) # O también len(valores), ya que deben ser del mismo tamaño

for i in range(longitud_listas):
    clave_actual = claves[i]
    valor_actual = valores[i]
    mi_diccionario[clave_actual] = valor_actual

print(mi_diccionario)