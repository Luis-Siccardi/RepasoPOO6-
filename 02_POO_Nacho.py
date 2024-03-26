
import random

class Luchador:

    def __init__(self, nombre, vida, ataque, defensa, velocidad):
        self.nombre = nombre
        self. vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad

    def resivirDanio(self, danioResivido):
        self.vida -= danioResivido * (danioResivido/self.defensa)
        if self.vida < 0:
            self.vida = 0
    
    def ataqueNormal(self, enemigo):
        infligeDanio = random.randint((self.ataque * 0.1), self.ataque)
        enemigo.resivirDanio(infligeDanio)
        print(f"{self.nombre} ataco a {enemigo.nombre} infligiendole {infligeDanio} de daño, dejandolo en {enemigo.vida} puntos de vida")

    def estarVivo(self):
        return self.vida > 0



class LuchadorFisico(Luchador):

    def __init__(self, nombre, vida, ataque, defensa, velocidad):
        super().__init__(nombre, vida, ataque, defensa, velocidad)
        self.culdown = 3
    
    def ataqueDoble(self, contrincante):
        self.ataqueNormal(contrincante)
        self.ataqueNormal(contrincante)



class LuchadorMental(Luchador):

    def __init__(self, nombre, vida, ataque, defensa, velocidad, poderCuracion):
        super().__init__(nombre, vida, ataque, defensa, velocidad)
        self.poderCuracion = poderCuracion
        self.culdown = 4
    
    def absorberFuerza(self, contrincante):
        self.ataqueNormal(contrincante)
        curacion = random.randint((self.poderCuracion/2), self.poderCuracion)
        self.vida += curacion
        print(f"{self.nombre} se ha curado {curacion} puntos de vida, quedando en {self.vida} puntos de vida")
        
        

class LuchadorEspiritual(Luchador):

    def __init__(self, nombre, vida, ataque, defensa, velocidad, poderCuracion):
        super().__init__(nombre, vida, ataque, defensa, velocidad)
        self.poderCuracion = poderCuracion
        self.culdown = 2

    def curarse(self):
        curacion = random.randint((self.poderCuracion/2), self.poderCuracion)
        self.vida += curacion
        print(f"{self.nombre} se ha curado {curacion} puntos de vida, quedando en {self.vida} puntos de vida")