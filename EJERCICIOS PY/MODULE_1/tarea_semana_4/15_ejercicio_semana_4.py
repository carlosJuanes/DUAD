#15  Cree un diagrama de flujo que le pida un numero al usuario y muestre “Fizz” si es divisible entre 3, “Buzz”
#  si es divisible entre 5, y “FizzBuzz” si es divisible entre ambos.

numero_ingresado=float(input("ingrese un numero= "))
if (numero_ingresado % 3==0)and(numero_ingresado % 5 ==0 ):
    print("fizzbuzz")
elif numero_ingresado % 3==0:
    print("fizz")
elif numero_ingresado % 5 ==0:
    print("buzz")