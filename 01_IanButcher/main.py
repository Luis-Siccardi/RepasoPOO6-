# Llamar a characters.py
from characters import Character

player1 = Character(input("Ingrese el nombre del personaje: "), 10, 150)
player2 = Character(input("Ingrese el nombre del personaje: "), 10, 150)

while player1.actualHealthPoints != 0 and player2.actualHealthPoints != 0:
    # Turnos 
    turno1 = int(input(f"Turno de {player1.name}, ingresa 1 para atacar y 2 para curarte!"))
    if turno1 == 1:
        player2.atack()
    elif turno1 == 2:
        player1.heal()   
     
    turno2 = input(f"Turno de {player2.name}")
    if turno2 == 1:
        player1.atack()
    elif turno2 == 2:
        player2.heal()

    if player1.actualHealthPoints <= 0 or player1.actualHealthPoints <= 0:
        print ("Juego finalizado uwu")
        break

