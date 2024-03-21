import  random

class Player:
    def __init__(self,name,life,dange):
        self.name = name
        self.life = life
        self.dange = dange

    def vivo(self):
        return self.life < 0
    
    def daño(self, dange):
        self.dange -= dange
        if self.life < 0:
            self.life = 0

    def ataque(self, enemy):
        dange = random(0, self.dange)
        enemy.daño(dange)
        print(f"{self.name} ataco a {enemy.name} inflige ")
        if not self.vivo:
            
        