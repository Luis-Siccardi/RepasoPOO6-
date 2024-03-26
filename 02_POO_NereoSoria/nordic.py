from creatures import Creature
import random

class Nordico(Creature):
    def __init__(self, ataque, vida):
        super().__init__(self, ataque, vida)
        self.ataque = random.randint(13, 20)
        self.vida = 130

    def esta_vivo(self):
        return self.vida > 0

    def recibir_danho(self, danho):
        self.vida = self.vida - danho
        if self.vida < 0:
            self.vida = 0
    def atacar(self, enemigo):
        danho = random.randint(0, self.ataque)
        enemigo.recibir_danho(danho)
        print(f"{self.nombre} ataca a {enemigo.nombre} y le inflige {danho}")
        if not enemigo.esta_vivo():
            print(f"{enemigo.nombre} ha sido vencido!")
