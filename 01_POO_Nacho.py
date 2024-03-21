import random



menu = '''#================================#
#           Pelear   -   1       #
#================================#
#          Curarse   -   0       #
#================================# 
# '''

Luch1 = '''#================================#
#                                #
#        Elige a tu jugador      #
#                                #
#================================#
#          Superman  -   0       #
#================================#
#          Macri     -   1       #
#================================#
#        Profe Luis  -   2       #
#================================# 
#          Dios      -   3       #
#================================#
#   Lebrone James    -   4       #
#================================#
# '''

Luch2 = '''#================================#
#                                #
#    Elige a tu contrincante     #
#                                #
#================================#
#          Superman  -   0       #
#================================#
#          Macri     -   1       #
#================================#
#        Profe Luis  -   2       #
#================================# 
#          Dios      -   3       #
#================================#
#   Lebrone James    -   4       #
#================================#
# '''



class Luchador:
    
    def __init__(self, nombre, vida, danio):
        self.nombre = nombre
        self.vida = vida
        self.danio = danio

    def resivirDanio(self, dañoResivido):
        self.vida -= dañoResivido
        if self.vida < 0:
            self.vida = 0
    
    def atacar(self, enemigo):
        infligeDanio = random.randint(0, self.danio)
        enemigo.resivirDanio(infligeDanio)
        print(f"{self.nombre} ataco a {enemigo.nombre} infligiendole {infligeDanio} de daño, dejandolo en {enemigo.vida} puntos de vida")

    def curarse(self):
        self.vida += 30
        print(f"{self.nombre} se ha curado 30 puntos de vida, quedando en {self.vida} puntos de vida")

    def estarVivo(self):
        return self.vida > 0



luchador1 = Luchador("Superman", 110, 45)
luchador2 = Luchador("Macri", 80, 55)
luchador3 = Luchador("Profe Luis", 50, 75)
luchador4 = Luchador("Dios", 150, 40)
luchador5 = Luchador("Lebron James", 100, 45)

jugadores = [luchador1, luchador2, luchador3, luchador4, luchador5]



def juego():

    jugador = int(input(Luch1))
    enemigo = int(input(Luch2))

    jugador1 = jugadores[jugador]
    jugador2 = jugadores[enemigo]
    
    turno = 0

    while jugador1.estarVivo() and jugador2.estarVivo():

        if turno == 0:
            decisionRival = random.randint(0,1)

            if decisionRival == 0:
                jugador2.curarse()
        
            elif decisionRival == 1:
                jugador2.atacar(jugador1)
            
            turno = 1
        
        if turno == 1:
            
            decisionJugador = int(input(menu))

            if decisionJugador == 0:
                jugador1.curarse()
        
            elif decisionJugador == 1:
                jugador1.atacar(jugador2)
            
            turno = 0
    
    if not jugador1.estarVivo():
        print(f"{jugador1.nombre} ha sido derrotado")
    
    elif not jugador2.estarVivo():
        print(f"{jugador2.nombre} ha sido derrotado")

juego()