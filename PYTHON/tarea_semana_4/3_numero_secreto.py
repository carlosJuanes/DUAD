#3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
# Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

#en este ejercicio tuve que ayudarme de la ia para llegar a una posible respuesta no a una respuesta como tal
#solicite ayuda para entemder paso a paso lo que el ejercicio pide.
#(investigar cómo generar un número aleatorio distinto cada vez que se ejecute.) yo entendi que tenia que 
#buscar la manera de que se generara una numero aleatorio despues de haber adivinado el numero secreto.

import random
jugar_nuevamente="si"
while jugar_nuevamente.lower()=="si":
    numero_secreto=random.randint(1,10)
    numero_ingresado=int(input(f"ingrese un numero del 1-10="))
    while numero_ingresado!=numero_secreto:
        print("por favor vuelva a intentarlo")
        numero_ingresado=int(input(f"ingrese un numero del 1-10="))
    print(f"felicidades el numero secreto es {numero_secreto}")
    jugar_nuevamente=input(f"quieres jugar nuevamente responde si para continuar")
print(f"fin del juego")
