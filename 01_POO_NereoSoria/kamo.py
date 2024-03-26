import time
import random

class PersonajeKamo:
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
        self.tiene_dope = False
        self.tiene_flechas_sangre = True
        self.tiene_rafagas_sangre = False
        self.tiene_rayo_sangre = False

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

    def atacar_dope(self):
        if self.tiene_dope:
            print(f"{self.nombre} utiliza la habilidad Dope y aumenta su ataque.")
            self.ataque += 10
        else:
            print("¡Kamo no ha aprendido la habilidad Dope!")

    def atacar_flechas_sangre(self, enemigo):
        if self.tiene_flechas_sangre:
            danho = self.ataque * 0.8
            enemigo.recibir_danho(danho)
            print(f"{self.nombre} dispara flechas de sangre a {enemigo.nombre} y le causa {danho} de daño.")
        else:
            print("¡Kamo no ha aprendido la habilidad Flechas de Sangre!")

    def atacar_rafagas_sangre(self, enemigo):
        if self.tiene_rafagas_sangre:
            danho = self.ataque * 1.5
            enemigo.recibir_danho(danho)
            print(f"{self.nombre} desata ráfagas de sangre sobre {enemigo.nombre} y le causa {danho} de daño.")
        else:
            print("¡Kamo no ha aprendido la habilidad Ráfagas de Sangre!")

    def atacar_rayo_sangre(self, enemigo):
        if self.tiene_rayo_sangre:
            danho = self.ataque * 2.5
            enemigo.recibir_danho(danho)
            print(f"{self.nombre} lanza un poderoso rayo de sangre hacia {enemigo.nombre} y le causa {danho} de daño.")
        else:
            print("¡Kamo no ha aprendido la habilidad Rayo de Sangre!")

    def recibir_danho(self, danho):
        if self.turnos_protegido > 0:
            danho = danho * 0.5  # El daño recibido se reduce a la mitad si está protegido
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
