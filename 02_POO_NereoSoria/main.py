from creatures import Creature
import random

def seleccion():
    raza_select = input("Seleccionar raza: 1 para nordico y 2 para orco ")
    if raza_select == "1":
        return  Creature.Nordico()
    elif raza_select == "2":
        return Creature.Orco()
    else:
        print ("Opción no válida")

def seleccion2():
    personajes_disponibles = [Creature.Nordico(), Creature.Orco()]
    return random.choice(personajes_disponibles)


def main():
    jugador1 = (seleccion)
    jugador2 = (seleccion2)
    while jugador1.esta_vivo() and jugador2.esta_vivo():
        jugador1.atacar(jugador2)
        
        if jugador2.esta_vivo():
            jugador2.atacar(jugador1)
    if jugador1.esta_vivo():
        print("Jugador 1 gana")
    else:
        print("Jugador 2 gana")
main()

