# Ejercicio 2

# Importar math random para criticos
import random

#comentario clase
lineas = '''
---------------------------------------------------------------
'''

class Creature:
    def __init__(self, name, health = 150, damage = 10, healingPotions = 10, agility = 3, vigor = 4, specialAtacks = 10):
        self.name = name
        self.maxHealth = health
        self.actualHealth = health
        self.damage = damage
        self.healingPotions = healingPotions
        self.agility = agility
        self.vigor = vigor
        self.specialAtacks = specialAtacks

    def atack(self, enemy):
        # Ver si fallo
        randomMiss = random.randint(0, enemy.agility)
        if randomMiss == 1:
            print(f"{self.name} ha fallado el ataque!")
        else:
            # Ver si es critico
            randomCrit = random.randint(0, self.vigor)
            if randomCrit == 1 and enemy.actualHealthPoints != 0:
                # El daño es %50 mas alto
                critHit = self.damage * 1.5
                print(lineas)
                print(f"Golpe critico a {self.name}!")
                
                #Quitar vida
                enemy.actualHealthPoints -= critHit

            #Golpe normal (No critico)
            elif randomCrit != 1 and self.actualHealthPoints != 0:
                print(lineas)
                print(f"Has atacado a {self.name}")
                
                # Quitar vida
                enemy.actualHealthPoints -= self.damage

            # Volver la vida a 0
            elif self.actualHealthPoints <= 0:
                enemy.actualHealthPoints = 0
                print(f"{self.name} ha sido derrotado! GG WP")

            

            print(f"{self.name} ahora tiene {self.actualHealthPoints}")
            print(lineas)

    # Metodo curar
    def heal(self):

        if self.actualHealthPoints != 0 and self.healingPotions != 0:
            self.healingPotions -= 1
            healed = random.randint(10, 30)
            self.actualHealthPoints += healed
        else:
            print("El personaje murio, no puedes curarlo!")
        
        if self.actualHealthPoints > self.maxHealthPoints:
            self.actualHealthPoints = self.maxHealthPoints
        
        print(lineas)
        print (f"{self.name} Se ha curado {healed}! Ahora tiene {self.actualHealthPoints}")
        print(lineas)


