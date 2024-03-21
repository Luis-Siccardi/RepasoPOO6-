# Ejercicio 1

# Importar math random para criticos
import random

#comentario clase
lineas = '''
---------------------------------------------------------------
'''

# Crear clase
class Character:
    # Crear constructor y atributos
    def __init__ (self, name, damage, maxHealtPoints):
        self.name = name
        self.damage = damage
        self.maxHealthPoints = maxHealtPoints
        self.actualHealthPoints = maxHealtPoints
        self.boostDamage = False
    
    # Esta vivo?
    # def is_alive(self):
    #    return (self.actualHealthPoints > 0)

    # Metodo atacar 
    def atack(self, damage):

        # Ver si es critico
        randomCrit = random.randint(0, 4)
        if randomCrit == 1 and self.actualHealthPoints != 0:
            # El daño es %50 mas alto
            critHit = damage * 1.5
            print(lineas)
            print(f"Golpe critico a {self.name}!")
            
            #Quitar vida
            self.actualHealthPoints -= critHit

        #Golpe normal (No critico)
        elif randomCrit != 1 and self.actualHealthPoints != 0:
            print(lineas)
            print(f"Has atacado a {self.name}")
            
            # Quitar vida
            self.actualHealthPoints -= damage

        # Volver la vida a 0
        elif self.actualHealthPoints <= 0:
            self.actualHealthPoints = 0
            print(f"{self.name} ha sido derrotado! GG WP")

        

        print(f"{self.name} ahora tiene {self.actualHealthPoints}")
        print(lineas)

    # Metodo curar
    def heal(self):

        if self.actualHealthPoints != 0:
            healed = random.randint(10, 30)
            self.actualHealthPoints += healed
        else:
            print("El personaje murio, no puedes curarlo!")
        
        if self.actualHealthPoints > self.maxHealthPoints:
            self.actualHealthPoints = self.maxHealthPoints
        
        print(lineas)
        print (f"{self.name} Se ha curado {healed}! Ahora tiene {self.actualHealthPoints}")
        print(lineas)

    # Metodo de escudo y defensa
    #boostDamageUses = 10
    # def boost(self, enemy):
    #    if self.boostDamageUses > 0:
     #       self.boostDamageUses -= 1
      #      enemy.self.boostDamage = True
       # else:
        #    print("Tu escudo esta roto, no puedes defenderte mas :c")