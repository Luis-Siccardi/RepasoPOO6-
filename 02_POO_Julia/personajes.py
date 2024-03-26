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

class Ogro (Personaje):
    def _init_(self, nombre, vida, ataque):
        super()._init_(nombre, vida, ataque )
