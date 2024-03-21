# Ejercicio 1

# Importar math random para criticos
import random



# Crear clase
class Character:
    # Crear constructor y atributos
    def __init__ (self, name, damage, maxHealtPoints):
        self.name = name
        self.damage = damage
        self.maxHealthPoints = maxHealtPoints
        self.actualHealthPoints = maxHealtPoints
    
    # Esta vivo?
    # def is_alive(self):
    #    return (self.actualHealthPoints > 0)

    # Funcion random crits
    def crits():
        randomCrit = random.randint(0, 4)
        return (randomCrit)

    # Metodo atacar 
    def atack(self):
        # Ver si es critico o no
        self.crits()
        if self.randomCrit == 1 and self.actualHealthPoints != 0:
            # El daño es %50 mas alto
            critHit = self.damage * 1.5
            print(f"Golpe critico a {self.name}!")
            # Quitar vida
            self.actualHealthPoints -= critHit

        #Golpe normal (No critico)
        elif self.randomCrit != 1 and self.actualHealthPoints != 0:
            print(f"Haz atacado a {self.name}")
            self.actualHealthPoints -= self.damage

        # Volver la vida a 0
        elif self.actualHealthPoints <= 0:
            self.actualHealthPoints = 0
            print(f"{self.name} ha sido derrotado! GG WP")

        print(f"{self.name} ahora tiene {self.actualHealthPoints}")

    # Metodo curar
    def heal(self, actualHealthPoints, maxHealthPoints):

        if actualHealthPoints != 0:
            self.actualHealthPoints += random.randint(10, 30)
        else:
            print("El personaje murio, no puedes curarlo!")
        
        if actualHealthPoints > maxHealthPoints:
            actualHealthPoints = maxHealthPoints
        print (f"{self.name} Se has curado {actualHealthPoints}!")
