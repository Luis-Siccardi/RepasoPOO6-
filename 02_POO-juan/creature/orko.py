from creature import Creature
import random
class orko(Creature):
    def __init__(self, name, life, dange, defence, magic_danger, defence_magic, extra_dange):
        super().__init__(name, life, dange, defence, magic_danger, defence_magic, extra_dange)

    def extra_dange(self, extra_dange, dange):
        extra_dange = random (0.0, 2.5)
        dange = dange * extra_dange
    
    def ataque(self, enemy):
        return super().ataque(enemy)
    