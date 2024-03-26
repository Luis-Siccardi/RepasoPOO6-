import  random
import  math

class Creature:
    def __init__(self,name,life,dange,defence,magic,defence_magic,extra_dange):
        self.name = name
        self.life = life
        self.dange = dange
        self.defence = defence
        self.magic = magic
        self.defence_magic = defence_magic
        self.extra_dange = extra_dange

    def vivo(self):
        return self.life > 0 
    
    def daño(self, dange):
        self.dange -= dange
        if self.life < 0:
            self.life = 0

    def ataque(self, enemy):
        dange = random(0, self.dange)
        enemy.daño(dange)
        print(f"{self.name} ataco a {enemy.name} inflige ")
        if not self.vivo:
            print(f"{enemy.name} masacro a {self.name}")

