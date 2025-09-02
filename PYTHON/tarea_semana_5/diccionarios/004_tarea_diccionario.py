sales = [
    {
        'date': '27/02/23',
        'customer_email': 'joe@gmail.com',
        'items': [
            {
                'name': 'Lava Lamp',
                'upc': 'ITEM-453',
                'unit_price': 65.76,
            },
            {
                'name': 'Iron',
                'upc': 'ITEM-324',
                'unit_price': 32.45,
            },
            {
                'name': 'Basketball',
                'upc': 'ITEM-432',
                'unit_price': 12.54,
            },
        ],
    },
    {
        'date': '27/02/23',
        'customer_email': 'david@gmail.com',
        'items': [
            {
                'name': 'Lava Lamp',
                'upc': 'ITEM-453',
                'unit_price': 65.76,
            },
            {
                'name': 'Key Holder',
                'upc': 'ITEM-23',
                'unit_price': 5.42,
            },
        ],
    },
    {
        'date': '26/02/23',
        'customer_email': 'amanda@gmail.com',
        'items': [
            {
                'name': 'Key Holder',
                'upc': 'ITEM-23',
                'unit_price': 3.42,
            },
            {
                'name': 'Basketball',
                'upc': 'ITEM-432',
                'unit_price': 17.54,
            },
        ],
    },
]

# Diccionario para almacenar el total de ventas por UPC
total_ventas_por_upc = {}

# Itera sobre cada venta en la lista 'sales'
for venta in sales:
    # Dentro de cada venta, accede a la lista de 'items'
    for item in venta['items']:
        # Extrae el UPC y el precio unitario de cada item
        upc = item['upc']
        unit_price = item['unit_price']

        # Verifica si el UPC ya existe en nuestro diccionario de totales
        if upc in total_ventas_por_upc:
            # Si existe, suma el precio unitario actual al total existente
            total_ventas_por_upc[upc] += unit_price
        else:
            # Si no existe, agrega el UPC como una nueva clave con su precio unitario
            total_ventas_por_upc[upc] = unit_price

# Imprime el diccionario con el total de ventas por UPC
print(total_ventas_por_upc)