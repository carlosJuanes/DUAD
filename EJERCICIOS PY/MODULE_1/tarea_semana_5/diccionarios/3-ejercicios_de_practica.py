# Nuestro diccionario de ejemplo
inventario_tienda = {
    "camisas": 150,
    "pantalones": 100,
    "zapatos": 75,
    "gorras": 50,
    "calcetines": 200
}

# Lista de claves a eliminar
claves_a_eliminar = ["zapatos", "gorras", "bolsos"] # "bolsos" no existe en el diccionario

print(f"Diccionario original: {inventario_tienda}")

for clave in claves_a_eliminar:
    if clave in inventario_tienda:
        valor_eliminado = inventario_tienda.pop(clave)
        print(f"Se eliminó '{clave}' con el valor '{valor_eliminado}'.")
    else:
        print(f"La clave '{clave}' no se encontró en el diccionario y no pudo ser eliminada.")

print(f"\nDiccionario final: {inventario_tienda}")
