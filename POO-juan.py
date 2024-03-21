import  random

class Player:
    def __init__(self,name,life,dange):
        self.name = name
        self.life = life
        self.dange = dange

    def vivo(self):
        return self.life > 0 
    
    def daño(self, dange):
        self.dange -= dange
        if self.life < 0:
            self.life = 0

 # personaje ataca, hace daño al enemigo
    def ataque(self, enemy):
        dange = random(0, self.dange)
        enemy.daño(dange)
        print(f"{self.name} ataco a {enemy.name} inflige ")
        if not self.vivo:
            print(f"{enemy.name} masacro a {self.name}")

print 
(
    "##########################################"
    "|                                        |"
    "|            eliga una clase             |"
    "|                                        |"
    "|              1- soldado                |"
    "|              2- caballero              |"
    "|              3- lancero                |"
    "|                                        |"
    "|                                        |"
    "##########################################"
)

clase = input ("inserte su clase aqui: ")

name = input ("inserte su nombre aqui: ")
if clase == 1 or "soldado":
    dange=50
    life=100
elif clase == 2 or "caballero":
    dange =25
    life =150
elif clase == 2 or "caballero":
    dange =100
    life =50

jugador1 = Player(name,life,dange)
enemy_1 = Player("rata", 10, 5)
enemy_2 = Player("bicho", 15, 5)
enemy_3 = Player("serpiente", 50, 20)
enemy_4 = Player("fastasma", 100, 50)
enemy_5 = Player("baso",1 ,0 )

enemys = [enemy_1,enemy_2,enemy_3,enemy_4,enemy_5]
# comenzar pelea   
while jugador1.vivo():
    if 

    else