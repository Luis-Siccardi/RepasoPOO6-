import time
import random

class PersonajeSukuna:
    def __init__(self, nombre, ataque, vida, energia_maldita, monedas=0):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = vida
        self.energia_maldita = energia_maldita
        self.monedas = monedas
        self.defendiendo = False
        self.turnos_protegido = 0
        self.tiene_golpe = True
        self.tiene_defensa = True
        self.tiene_patada = True
        self.tiene_corte = True
        self.tiene_rafagas_corte = False
        self.tiene_blackbox = True
        self.tiene_lanza_fuego = True
        self.tiene_expansion = True
        self.tiene_esquive = True
    def esta_vivo(self):
        return self.vida > 0

    def atacar_golpe(self, enemigo):
        if self.tiene_golpe:
            danho = self.ataque * 2
            enemigo.recibir_danho(danho)
            print(f"{self.nombre} realiza un golpe potente y causa {danho} de daño a {enemigo.nombre}.")
        else:
            print("¡Kamo no ha aprendido la habilidad Golpe!")

    def atacar_defensa(self):
        if self.tiene_defensa:
            print(f"{self.nombre} se pone en posición defensiva y aumenta su defensa.")
            self.defendiendo = True
        else:
            print("¡Kamo no ha aprendido la habilidad Defensa!")

    def atacar_patada(self):
        if self.tiene_patada:
            danho = self.ataque + 10
            self.energia_maldita - 20
        else:
            print("caiate")

    def atacar_corte(self, enemigo):
        if self.tiene_corte:
            danho = self.ataque * 0.8
            enemigo.recibir_danho(danho)
            print(f"{self.nombre} dispara flechas de sangre a {enemigo.nombre} y le causa {danho} de daño.")
        else:
            print("¡Kamo no ha aprendido la habilidad Flechas de Sangre!")

    def atacar_blackbox(self):
        if self.tiene_blackbox:
            print(f"{self.nombre} Ha abierto la caja negra...")
        else:
            print("¡Kamo no ha aprendido la habilidad Ráfagas de Sangre!")

    def atacar_lanza_fuego(self, enemigo):
        if self.tiene_lanza_fuego:
            if self.tiene_blackbox == True:
                danho = self.ataque * 2.5
                enemigo.recibir_danho(danho)
                print(f"{self.nombre} lanza un poderoso rayo de fuego hacia {enemigo.nombre} y le causa {danho} de daño.")
            else:
                ("No has abierto la Caja Negra")
        else:
            print("No puedes usar este ataque")
    def atacar_expansion(self, enemigo):
        if self.tiene_expansion and self.tiene_blackbox:
            time.sleep(1)
            print("EXPANSION DE DOMINIO.......")
            time.sleep(1)
            print("PANDEMONIO.")
            danho = 20000
            enemigo.recibir_danho(danho)
            print(f"{self.nombre} usa Expansión de Dominio y aniquila a {enemigo.nombre}.")

    def recibir_danho(self, danho):
        if self.turnos_protegido > 0:
            danho = danho * 0.5 
        self.vida -= danho
        if self.vida < 0:
            self.vida = 0

    def defender(self):
        if self.tiene_defensa:
            print(f"{self.nombre} se pone en posición defensiva y aumenta su defensa.")
            self.defendiendo = True
        else:
            print("¡Kamo no ha aprendido la habilidad Defensa!")

    def reanudar_turno(self):
        if self.defendiendo:
            print(f"{self.nombre} deja de defenderse.")
            self.defendiendo = False
        if self.turnos_protegido > 0:
            print(f"{self.nombre} ya no está protegido.")
            self.turnos_protegido -= 1

    def barra_vida(self):
        barra = "*" * int(self.vida / 10)
        return f"{self.nombre}: {barra} ({self.vida} HP)"

    def barra_energia_maldita(self):
        barra = "*" * int(self.energia_maldita / 10)
        return f"{self.nombre} (EM): {barra} ({self.energia_maldita} EM)"
