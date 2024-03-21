import random

class jugador:
    def __init__(self, nombre, vida, poderataque):
        self.nombre = nombre
        self.vida = vida
        self.poderataque = poderataque

    def atacar(self, otro_personaje):
        daño = random.randint(0, self.poderataque)
        otro_personaje.recibir_ataque(daño)

    def recibir_ataque(self, daño):
        self.vida -= daño
        print(f"{self.nombre} recibió {daño} puntos de daño.")

    def esta_vivo(self):
        return self.vida > 0


def lucha(personaje1, personaje2):
    print("¡Comienza la batalla!")
    print(f"{personaje1.nombre} vs {personaje2.nombre}")

    while personaje1.esta_vivo() and personaje2.esta_vivo():
        personaje1.atacar(personaje2)
        if not personaje2.esta_vivo():
            print(f"{personaje1.nombre} dice con tono musical: Esta fue la nochee mas linda del mundo, aun que nos durara tan solo un segundoo")
            break

        personaje2.atacar(personaje1)
        if not personaje1.esta_vivo():
            print(f"{personaje2.nombre} a la parrilla")
            break

personaje1= personaje("spiderman", 100, 30)
personaje2= personaje("vegetta", 100, 25)

lucha(personaje1, personaje2)
