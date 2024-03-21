import random

class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.poder_ataque = ataque
#constructor

    def atacar(self, personaje2):
        danio = random.randint(0, self.poder_ataque)
        personaje2.recibir_danio(danio)
        print(self.nombre, "atacó a" ,personaje2.nombre, "y le causó ", danio, "de daño.")

#Metodo atacar, indica que el daño va a ser igual a un random, dps el personaje recibe ese daño y hace un print a la acción
    def recibir_danio(self, danio):
        self.vida -= danio
        #if self.vida >= 0:
            #print("A " , self.nombre, " Le queda" , self.vida)

#Metodo recibir daño, le saca el daño a la vida y le dice cuanto tiene, lo comenté porque me funciona mal
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