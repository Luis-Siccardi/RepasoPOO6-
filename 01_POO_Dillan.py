import random

class Peleador:
    def __init__(self, nombre, vida, min_poder, max_poder):
        self.nombre = nombre
        self.vida = vida
        self.min_poder = min_poder
        self.max_poder = max_poder
    
    def Esta_vivo(self):
        return self.vida > 0
    
    def Recibir_danho(self, danho):
        self.vida -= danho
        if self.vida < 0:
            self.vida = 0
        return self.vida
    
    def Atacar_enemigo(self, enemigo):
        if self.Esta_vivo():
            danho = random.randint(self.min_poder, self.max_poder)
            print(self.nombre + " ataca a " + enemigo.nombre + " con " + str(danho) + " de poder.")
            enemigo.Recibir_danho(danho)
            if not enemigo.Esta_vivo():
                print(enemigo.nombre + " ha sido derrotado!")


class Peleadores:
    def __init__(self, fighter1_name, fighter1_health, fighter1_min_power, fighter1_max_power, 
                 fighter2_name, fighter2_health, fighter2_min_power, fighter2_max_power):
        
        self.fighter1 = Peleador(fighter1_name, fighter1_health, fighter1_min_power, fighter1_max_power)

        self.fighter2 = Peleador(fighter2_name, fighter2_health, fighter2_min_power, fighter2_max_power)
        
    def Combat(self):
        while True:
            self.fighter1.Atacar_enemigo(self.fighter2)
            if not self.fighter2.Esta_vivo():
                print(self.fighter1.nombre + " ha ganado!")
                break
            self.fighter2.Atacar_enemigo(self.fighter1)
            if not self.fighter1.Esta_vivo():
                print(self.fighter2.nombre + " ha ganado!")
                break

game = Peleadores("Batman", 100, 15, 25, "Superman", 100, 15, 25)
game.Combat()