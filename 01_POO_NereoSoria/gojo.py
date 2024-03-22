import random
import time

class PersonajeGojo:
    def __init__(self, nombre, ataque, vida, energia_maldita, monedas=100):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = vida
        self.energia_maldita = energia_maldita
        self.monedas = monedas
        self.defendiendo = False  
        self.tiene_expansion = True
        self.tiene_purpura = False
        self.tiene_infinito = False
        self.turnos_protegido = 0 

    def reanudar_turno(self):
        self.defendiendo = False
        print(f"{self.nombre} ha reanudado su turno.")

    def defender(self):
        self.defendiendo = True
        print(f"{self.nombre} se ha puesto en posición defensiva.")

    def dejar_de_defender(self):
        self.defendiendo = False
        print(f"{self.nombre} deja de defenderse.")

    def esta_vivo(self):
        return self.vida > 0

    def recibir_danho(self, danho):
        if self.turnos_protegido > 0:
            print(f"{self.nombre} está protegido y no recibe daño.")
            self.turnos_protegido -= 1
        else:
            self.vida = max(0, self.vida - danho)
            print(f"{self.nombre} recibe {danho} de daño.")

    def atacar_rojo(self, enemigo):
        if self.energia_maldito >= 20:
            danho = random.randint(0, self.ataque)
            enemigo.recibir_danho(danho)
            print(f"{self.nombre} ataca a {enemigo.nombre} con ataque Rojo y le inflige {danho} de daño.")
        else:
            print("No tienes suficiente energía maldita para usar el ataque Azul.")


    def atacar_azul(self, enemigo):
        if self.energia_maldita >= 20:
            enemigo.recibir_danho(5)
            self.energia_maldita -= 20
            print(f"{self.nombre} ataca a {enemigo.nombre} con ataque Azul y le inflige 5 de daño.")
        else:
            print("No tienes suficiente energía maldita para usar el ataque Azul.")

    def atacar_infinito(self, enemigo):
        if self.tiene_infinito and self.energia_maldita >= 40:
            self.turnos_protegido = 2 
            print(f"{self.nombre} utiliza el ataque Infinito. Estará protegido por 2 turnos.")
            self.energia_maldita -= 40
        else:
            print("No has comprado el ataque Infinito.")
        
    def atacar_purpura(self, enemigo):
        if self.tiene_purpura and self.energia_maldita >= 60:
            danho = random.randint(20, 40)
            enemigo.recibir_danho(danho)
            print(f"{self.nombre} ataca a {enemigo.nombre} con ataque Púrpura y le inflige {danho} de daño.")
            self.energia_maldita -= 60
            if danho > 20:
                self.monedas += 10
                print(f"¡{self.nombre} recibe 10 monedas adicionales por infligir más de 20 de daño!")
        else:
            print("No has comprado el ataque Púrpura.")

    def atacar_expansion(self, enemigo):
        if self.tiene_expansion and self.energia_maldita == 100:
            satoru = '''
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣾⣿⡟⢹⣿⣿⣿⣿⡽⣿⣿⡟⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡌⣿⣿⣿⣷⡝⢿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⣸⣿⠃⠀⠘⢿⣿⣿⣿⡇⠋⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡌⢿⣿⣿⣿⣾⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡋⠉⠀⠀⠀⣿⠃⠀⠀⠀⠘⠙⣿⣿⡇⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣎⢻⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⣠⡦⣰⠃⠀⣰⡆⠀⠀⠈⠸⣿⣷⠀⠀⠈⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡎⢿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⡿⣿⣿⣿⢣⣾⢯⣾⡿⠋⠀⠀⠀⠚⠻⠃⡏⠀⣼⣿⡇⠀⠀⠀⠀⠹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⡌⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣻⣿⣿⢓⡿⠋⣼⡿⠁⠀⢀⢬⣀⠀⠀⠸⠀⠀⠉⠻⢇⠀⢠⣷⣄⠀⠹⣇⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⢘⣿⣿⣿
                ⣿⣿⣿⣿⡟⣸⣿⢏⡞⠁⢰⡟⠀⠀⠀⠁⠈⠉⠑⠁⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⡄⠙⡌⡁⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⣿⣿⣇⣻⡿⣿
                ⣿⣿⣿⣿⠃⣿⡏⠌⠀⠀⠟⠀⠀⠀⣠⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⠀⠀⢠⣾⠀⠀⠀⠀⠀⣀⣠⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣧⢻
                ⣻⣿⣿⠏⠈⣿⠃⠀⠀⠀⠀⢀⣴⣿⢋⠼⠀⢟⢻⣿⣴⡄⠀⠀⠎⣠⣀⢠⣿⣿⣿⣿⠀⠀⠀⠁⠀⠀⠀⢠⡘⣿⠟⠧⠒⠨⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⢘⣿⣿⣟
                ⣿⣿⡿⠀⢠⡟⠀⠀⠀⠀⢠⣿⣿⣯⡀⠀⠀⣀⣼⣿⣿⡗⠀⠀⠐⢹⣿⡄⢿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⢻⣿⣼⣦⡀⠀⠀⢀⣼⣆⣳⡄⠀⠀⠀⠀⠀⠀⢿⠸⢿⣿⢻
                ⣿⣿⠇⠀⢐⡇⠀⡖⠀⠀⠈⠿⡿⠛⠉⠛⠋⠉⠉⠙⠁⠀⠠⣤⣶⣿⣿⣿⣿⠿⠻⠧⠀⠀⠀⠀⠀⠀⠀⠀⠙⠉⠉⠉⠉⠉⠙⠻⢿⠿⠃⠀⠀⠀⠀⠀⠀⢸⠀⠀⠹⣧
                ⣿⣿⠀⠀⠀⠇⣴⣾⣶⣤⣀⠀⠀⠀⠀⠀⣀⣀⣀⣠⣤⣶⣿⣿⣿⣿⣿⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡀⠀⠸⠀⠀⠀⠈
                ⣿⡏⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡧⠀⠀⠀⠀⠀⠀
                ⣿⡇⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⢸⣷⣶⣿⣿⣿⣿⣿⣿⣿⣁⡀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠄⠀⠀⠀⠀⠀
                ⢻⡇⠀⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠀⠀⠀⠀⠀⠀⠀⠸⡟⣽⠀⠀⠀⠀⠀⠀
                ⢸⡇⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠹⠇⠰⠉⠾⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⢈⣿⣉⠀⠀⠀⠀⠀⠀
                ⠀⠁⠀⠀⢈⣿⣿⣿⣿⣿⣿⡿⠋⠉⣹⣿⣿⣿⣿⣿⣿⠿⠟⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠉⠉⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣷⣤⠄⠀⠀⠀⠀⢘⢍⡇⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠘⢿⣿⣿⣿⠛⠉⠀⣠⣾⣿⣿⡿⠟⠋⢉⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣀⡈⠙⠿⣿⣿⣿⣟⠁⠀⠀⠀⠀⠀⠘⠛⠃⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠸⣿⣿⡇⠀⠀⠀⠈⠋⠉⠉⢀⣤⣶⣿⣿⣿⡿⠿⠿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣷⣦⣀⠉⠛⠋⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠰⢾⡿⠯⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠹⠿⡷⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠈⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠺⣛⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠋⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀.⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀.⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢷⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣼⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
            print(satoru)
            time.sleep(1)
            print("EXPANSION DE DOMINIO.......")
            time.sleep(1)
            print("INFINITO.")
            danho = 20000
            enemigo.recibir_danho(danho)
            self.energia_maldita -= 100
            print(f"{self.nombre} usa Expansión de Dominio y aniquila a {enemigo.nombre}.")
        
            

    def defender(self):
        self.energia_maldita += 30
        print(f"{self.nombre} se defiende y recupera 30 de Energía Maldita.")

    def barra_vida(self):
        barra = "*" * int(self.vida / 10)
        return f"{self.nombre}: {barra} ({self.vida} HP)"

    def barra_energia_maldita(self):
        return f"{self.nombre} (EM): {self.energia_maldita}"

    def barra_moneda(self):
        return f"{self.nombre}: {self.monedas} monedas"
