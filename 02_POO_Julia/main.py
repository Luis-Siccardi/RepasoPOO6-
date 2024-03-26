import random
from personajes import Personaje

def jugar_batalla(personaje1, personaje2):
    while personaje1.vida > 0 and personaje2.vida > 0:
        personaje1.atacar(personaje2)
        if personaje2.vida <= 0:
            print(personaje1.nombre, "ganó la batalla! :D")
            break
        
#Jugar batalla, mientras la vida de los personajes sea mayor a 0 el primer personaje ataca al otro con el método atacar, y si le queda 0 dice que ganó el otro
        personaje2.atacar(personaje1)
        if personaje1.vida <= 0:
            print(personaje2.nombre, "ganó la batalla! :D")
            break
#Si este sobrevive ataca el otro, y así hasta que uno queda sin vida

def main():
    nombre1 = str(input("Ingresá el nombre del primer personaje "))
    nombre2 = str(input("Ingresá el nombre del segundo personaje "))
    personaje1 = Personaje(nombre1, 100, 10)
    personaje2 = Personaje(nombre2, 100, 10)

    print("Que empiece la batalla!!!")
    jugar_batalla(personaje1, personaje2)
main()
#Llamamos al main que pregunta el nombre y llama al metodo jugar batalla con los dos personajes