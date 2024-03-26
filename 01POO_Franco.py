import random

class Personaje:
    def __init__(self, nombre, vida, poder_ataque):
        self.nombre = nombre
        self.vida = vida
        self.poder_ataque = poder_ataque

    def atacar(self, otro_personaje):
        daño = random.randint(0, self.poder_ataque)
        otro_personaje.recibir_ataque(daño)

    def recibir_ataque(self, daño):
        self.vida -= daño
        print(f"{self.nombre} recibió {daño} puntos de daño.")

    def esta_vivo(self):
        return self.vida > 0


def batalla(personaje1, personaje2):
    print("¡Comienza la batalla!")
    print(f"{personaje1.nombre} vs {personaje2.nombre}")

    while personaje1.esta_vivo() and personaje2.esta_vivo():
        personaje1.atacar(personaje2)
        if not personaje2.esta_vivo():
            print(f"{personaje1.nombre} dice con tono musical: Esta fue la noche más linda del mundo, aunque nos durara tan solo un segundo")
            break

        personaje2.atacar(personaje1)
        if not personaje1.esta_vivo():
            print(f"{personaje2.nombre} a ganado")
            break

def menu_seleccion_personaje():
    print("¡Bienvenido al juego de batalla!")
    print("Selecciona tu personaje:")
    print("1. Goku")
    print("2. Freezer")
    print("3. Vegeta")
    print("4. Piccolo")
    print("5. Majin-Boo")
    print("6. Cell")
    
    opcion = int(input("Elige un número para seleccionar tu personaje: "))
    if opcion == 1:
        return Personaje("Goku", 100, 30)
    elif opcion == 2:
        return Personaje("Freezer", 100, 25)
    elif opcion == 3:
        return Personaje("Vegeta", 100, 28)
    elif opcion == 4:
        return Personaje("Piccolo", 100, 27)
    elif opcion == 5:
        return Personaje("Majin-Boo", 100, 32)
    elif opcion == 6:
        return Personaje("Cell", 100, 29)
    else:
        print("Opción no válida. Por favor, selecciona un número del 1 al 6.")
        return menu_seleccion_personaje()

def main():
    personaje_jugador = menu_seleccion_personaje()
    personaje_enemigo = Personaje("Jiren", 100, 40) 
    batalla(personaje_jugador, personaje_enemigo)

if __name__ == "__main__":
    main()