#6. Cree un pseudocódigo que le pida un `precio de producto` al usuario,
#calcule su descuento y muestre el precio final tomando en cuenta que:
    #1. Si el precio es menor a 100, el descuento es del 2%.
    #2. Si el precio es mayor o igual a 100, el descuento es del 10%.

precio_del_producto=float(input(f"ingrese el precio del producto: "))
if precio_del_producto<100:
    descuento=precio_del_producto*0.02
else:
   descuento=precio_del_producto*0.1

print(f"el precio final del producto es de {precio_del_producto-descuento:.2f}")