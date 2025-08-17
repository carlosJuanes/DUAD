#6  Create an algorithm that asks the user for a product price,
#  then calculates its discount and displays the final price, taking into account that:

#If the price is less than 100, the discount is 2%.
#If the price is 100 or greater, the discount is 10%.

product_price=float(input(f"enter the product price: "))
if product_price<100:
    discount=product_price*0.02
else:
   discount=product_price*0.1

print(f"the final product price is {product_price-discount:.2f}")