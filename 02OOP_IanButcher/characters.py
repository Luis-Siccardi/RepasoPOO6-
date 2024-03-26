from creature import Creature
from creature import lineas
class Human(Creature):
    def __init__(self, name, health=100, damage=10, healingPotions=10, agility=5, vigor=4, specialAtacks = 15):
        super().__init__(name, 100, 10, 10, 5, 4, 15)

    # Ataque inesquivable
    def swing(self, enemy):
        if self.specialAtacks != 0:
            self.specialAtacks -= 1
            trialAgility = enemy.agility 
            enemy.agility = 0
            self.atack(enemy)
            print(lineas)
            print(f"{self.name} ha realizado un ataque inesquvable a {enemy.name}")
            print(lineas)
            enemy.agility = trialAgility
        else:
            print("No tienes mas ataques especiales")

    def rage(self, enemy):
        if self.specialAtacks != 0:
            self.specialAtacks -= 1
            trialDamage = self.damage
            self.damage = self.damage * 1.5
            self.atack(enemy)
            print(lineas)
            print(f"{self.name} se enojo! Hizo {self.damage} de daño a {enemy.name}")
            print(lineas)
            self.damage = trialDamage
        else:
            print("No tienes mas ataques especiales")

    restUses = 5
    def rest (self):
        if self.restUses != 0:
            self.specialAtacks += 1
        else:
            print("No puedes descansar mas dormilon/a")


# Clase bruja pueda crear pociones
class Witch (Creature):
    def __init__(self, name, health=150, damage=10, healingPotions=10, agility=3, vigor=4, specialAtacks = 15):
        super().__init__(name, 125, 10, 10, 5, 3, 20)

    def phoenixCannon (self, enemy):
        trialDamage = self.damage * 2
        self.atack(enemy)
        print(lineas)
        print(f"{self.name} ha utilizado Phoenix Cannon!")
        print(lineas)

    