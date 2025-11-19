class Product:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

class Inventory:
    def __init__(self):
        self.products=[]

    def add_products(self, product):
        self.products.append(product)


    def display_products(self):
        print("The inventory of the products is:")
        print("----------------------------------")
        for product in self.products:
            print(f"Product= {product.name}, Price= {product.price}, Quantity= {product.quantity} ")
        print("----------------------------------")

    def get_total(self):
        total_value=0
        for product in self.products:
            total=product.price * product.quantity
            total_value+=total
        return total_value

Product_1=Product("apple", 5, 1)
Product_2=Product("lemon", 1,5)
Product_3=Product("orange", 5,3)
my_Inventory=Inventory()

my_Inventory.add_products(Product_1)
my_Inventory.add_products(Product_2)
my_Inventory.add_products(Product_3)

my_Inventory.display_products()
print(f"The total value of the inventory is = {my_Inventory.get_total()} ")
