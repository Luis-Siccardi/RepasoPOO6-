import random

class Personaje:
    def __init__(self, nombre, ataque, habilidad, arma):
        self.nombre = nombre
        self.vida = 150
        self.ataque = ataque
        self.habilidad = habilidad
        self.arma = arma

    def atacar(self, contrario):
        damage = random.randint(0, self.ataque) + self.arma.daño
        contrario.recibir_danio(damage)
        print(f"{self.nombre} ataca a {contrario.nombre} con {self.arma.nombre} y causa {damage} de daño")

    def recibir_danio(self, danio):
        self.vida -= danio
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nombre} ha sido derrotado")
        else:
            print(f"{self.nombre} recibe {danio} de daño. Queda con {self.vida} de vida")

class Habilidad:
    def __init__(self, nombre, desc):
        self.nombre = nombre
        self.desc = desc

class Arma:
    def __init__(self, nombre, danio):
        self.nombre = nombre
        self.daño = danio

espada = Arma("Espada", 15)
palo = Arma("Palo", 25)
martillo = Arma("Martillo", 20)

escudo = Habilidad("Escudo", "Protección al daño recibido")
velocidad = Habilidad("Velocidad", "Aumenta la velocidad de movimiento del personaje")
hechizo = Habilidad("Hechizo", "El personaje lanza una bola de hielo restando daño")

Celine = Personaje("Celine", 20, escudo, espada)
Kanye = Personaje("Kanye", 20, velocidad, martillo)
Taylor = Personaje("Taylor", 15, hechizo, palo)

print("Elige un personaje")
print("-------------------")
print("1. Celine")
print("2. Kanye")
print("3. Taylor")
opcion = int(input("Escriba una de las opciones: "))

if opcion == 1:
    jugador = Celine 
elif opcion == 2:
    jugador = Kanye
else:
    jugador = Taylor

while Celine.vida > 0 and Kanye.vida > 0 and Taylor.vida > 0:
    print(f"Turno de {jugador.nombre}")
    print("1. Atacar")
    print("2. Usar habilidad")
    accion = int(input("Seleccione una opción: "))

    if accion == 1:
        objetivos = [obj for obj in [Celine, Kanye, Taylor] if obj != jugador]
        objetivo = random.choice(objetivos)
        jugador.atacar(objetivo)
    else:
        print(f"{jugador.nombre} usa la habilidad {jugador.habilidad.nombre}: {jugador.habilidad.desc}")

    if Celine.vida <= 0 or Kanye.vida <= 0 or Taylor.vida <= 0:
        break

    enemigo = random.choice([Celine, Kanye, Taylor])
    while enemigo == jugador:
        enemigo = random.choice([Celine, Kanye, Taylor])

print("Fin del juego")



