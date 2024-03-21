import random
class personaje:
    #Constructor define nombre vida y daño, define los atributos
    def __init__(self,nombre, cantidadVida, poderAtaque) :
        self.nombre = nombre
        self.cantidadVida = cantidadVida
        self.poderAtaque= poderAtaque

    #Si su vida es mayor a cero devuelve la cantidad de vida
    def estavivo(self):
        return self.cantidadVida > 0

    # De acuerdo al daño
    def recibirdaño(self, danio):
        #Se guarda la vida como si misma menos el daño recibido
        self.cantidadVida= self.cantidadVida - danio
        # Si la vida es menor a 0 la volvemos 0 para que no imprima vida -1 o algo asi
        if self.cantidadVida < 0:
            self.cantidadVida = 0

    #Al crear el objeto definimos un enemigo
    def atacarenemigo(self,enemigo):
        #Numero de daño aleatorio
        danio= random.randint(0,self.poderAtaque)
        #El enemigo ejecuta el metodo recibirDaño
        enemigo.recibirdaño(danio)
        print(f"Has hecho {danio} daño")
        return danio

def main():
    nombrejugador= str(input("ingrese el nombre del jugador1 "))
    jugador1=personaje(nombrejugador,100,20)
    print(nombrejugador)
    nombrejugador= str(input("ingrese el nombre del jugador2"))
    jugador2=personaje(nombrejugador,100,20)
    print(nombrejugador)

    #mientras los dos jugadores esten vivos
    while jugador1.estavivo() and jugador2.estavivo():
        #Jugador uno define como enemigo a jugador 2 y ejecuta el
        jugador1.atacarenemigo(jugador2)
        if jugador2.estavivo():
            jugador2.atacarenemigo(jugador1)
         
            
    if jugador1.estavivo():
        print(f"{jugador1.nombre} gana")
    else:
        print(f"{jugador2.nombre} gana")


main()
