import random

class Luchadores:
    vida = 100

    def __init__ (self, nombre, poder):
        self.nombre = nombre
        # Limitar el poder máximo a 90
        self.poder = min(poder, 90)
        self.vida = Luchadores.vida

    def con_vida (self):
        return self.vida > 0

    def recibir_danho(self, danho):
        self.vida -= danho
        if self.vida < 0:
            self.vida = 0

    def atacar_enemigo(self, enemigo):
        danho = random.randint(0, self.poder)
        print(f"{self.nombre} le pego a {enemigo.nombre} y el golpe le infligio {danho} de daño.")
        enemigo.recibir_danho(danho)
        self.mostrar_vida()
        enemigo.mostrar_vida()
        if not enemigo.con_vida():
            print(f"{enemigo.nombre} a sido derrotado por {self.nombre} con un ferroz ataque! 💀")

    def mostrar_vida(self):
        barra_vida = "█" * int(self.vida / 5) + "░" * int((100 - self.vida) / 5)
        print(f"Vida de {self.nombre}: [{barra_vida}]")

def main():
    nombre_jugador1 = input("Ingrese el nombre del jugador 1: ")
    poder_jugador1 = int(input("Ingrese el poder del jugador 1 (máximo 90): "))
    jugador1 = Luchadores(nombre_jugador1, poder_jugador1)

    nombre_jugador2 = input("Ingrese el nombre del jugador 2: ")
    poder_jugador2 = int(input("Ingrese el poder del jugador 2 (máximo 90): "))
    jugador2 = Luchadores(nombre_jugador2, poder_jugador2)

    while jugador1.con_vida() and jugador2.con_vida():
        jugador1.atacar_enemigo(jugador2)
        if not jugador2.con_vida():
            print(f"{jugador2.nombre} ha sido derrotado por {jugador1.nombre}! 💀")
            break
        jugador2.atacar_enemigo(jugador1)
        if not jugador1.con_vida():
            print(f"{jugador1.nombre} ha sido derrotado por {jugador2.nombre}! 💀")
            break

main()
