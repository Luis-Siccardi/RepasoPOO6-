# Llamar a characters.py
from characters import Character

player1 = Character(input("Ingrese el nombre del personaje: "), 10, 150)
player2 = Character(input("Ingrese el nombre del personaje: "), 10, 150)

#players = [player1, player2]

while player1.actualHealthPoints != 0 and player2.actualHealthPoints != 0:
    # Turnos 
    # idea de hacerlos con for no me saliofor player in players:
    
    turno1 = int(input(f"Turno de {player1.name}, ingresa 1 para atacar, 2 para curarte y 3 para defenderte del proximo ataque!"))
    if turno1 == 1:
        player2.atack(15)
    elif turno1 == 2:
        player1.heal() 
    elif turno1 == 3:
        player1.shield(player2)  
     
    turno2 = int(input(f"Turno de {player2.name} ingresa 1 para atacar, 2 para curarte y 3 para defenderte del proximo ataque!"))
    if turno2 == 1:
        player1.atack(15)
    elif turno2 == 2:
        player2.heal()
    elif turno1 == 3:
        player2.shield(player1) 

    if player1.actualHealthPoints <= 0 or player2.actualHealthPoints <= 0:
        print ("Juego finalizado uwu")
        break

 