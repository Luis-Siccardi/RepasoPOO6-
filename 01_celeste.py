import random 
class Personajes:
    vida=100

    def __init__(self,vida,ataque,nombre) :
        self.vida= vida
        self.ataque=ataque
        self.nombre=nombre

        def esta_vivo (self):
            return esta_vivo > 0
        def daño (self,daño):
            self.vida -= daño
            if self.vida <0 :
                self.vida =0
        def atacar_enemigo(self , enemigo):
            daño=random.randint(0,self.ataque)
            enemigo.recibir_daño(daño)
            print(f"{self.nombre} ataca a {enemigo.nombre} le inflinge{daño}")

            if not enemigo.esta_vivo():
                print(f"{enemigo.nombre} fue vencido")


    def main ():
        Red=Personajes ("Red",100,20)
        Blue=Personajes ("Blue",100,20)

        while Red.esta_vivo and Blue.esta_vivo ():

           Red.atacar_enemigo(Blue) 
        
        if Blue.esta_vivo :
            Blue.atacar_enemigo (Red)

        if Red.esta_vivo():

            print(f"{Red.nombre} GANA¡")
        else :
            print(f"{Blue.nombre} GANA ¡")

              






        

    


        
        


        