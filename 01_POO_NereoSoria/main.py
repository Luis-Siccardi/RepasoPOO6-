import time
import random
from gojo import PersonajeGojo
from kamo import PersonajeKamo
from sukuna import PersonajeSukuna
from choicesgojo import opciongojo
from choiceskamo import opcionkamo
from choicessukuna import opcionsukuna
from menu_compras import mostrar_menu_compras

def seleccionar_personaje():
    while True:
        print("Selecciona un personaje para jugar:")
        print("1. Gojo")
        print("2. Kamo")
        print("3. Sukuna")
        print("4. Fushiguro")
        print("5. Mahito")
        opcion1 = input("Elige una opción: ")

        if opcion1 == "1":
            return PersonajeGojo("Gojo", 30, 200, 100) 
        elif opcion1 == "2":
            return PersonajeKamo("Kamo", 25, 220, 120) 
        elif opcion1 == "3":
            return PersonajeSukuna("Sukuna", 40, 220, 150)  
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3. faltan añadir personajes jeje lo hago despues")

def menu_inicial():
    while True:
        print("¡Bienvenido al juego!")
        print("1. Jugar")
        print("2. Menú de compras")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            main()
        elif opcion == "2":
            mostrar_menu_compras()
        else:
            print("Opción no válida. Por favor, selecciona 1 o 2.")

def seleccionar_personaje_aleatorio():
    personajes_disponibles = [PersonajeGojo("Gojo", 30, 200, 100), PersonajeKamo("Kamo", 25, 220, 120), PersonajeSukuna("Sukuna", 40, 220, 150)]
    return random.choice(personajes_disponibles)



def main():
    jugador1 = seleccionar_personaje()
    jugador2 = seleccionar_personaje_aleatorio()
    
    turnos_efectividad_infinito = 0

    while jugador1.esta_vivo() and jugador2.esta_vivo():
        print(jugador1.barra_vida())
        print(jugador1.barra_energia_maldita())
        print(" " * 20 + "|" + " " * 20)
        print(jugador2.barra_vida())
        print(jugador2.barra_energia_maldita())
        if isinstance(jugador1, PersonajeGojo):
            opciongojo(jugador1, jugador2)
        elif isinstance(jugador1, PersonajeKamo):
            opcionkamo(jugador1, jugador2)
        elif isinstance(jugador1, PersonajeSukuna):
            opcionsukuna(jugador1, jugador2)
        if isinstance(jugador2, PersonajeGojo):
            if jugador2.esta_vivo() and not jugador1.defendiendo:
                decision_jugador2 = random.choice(["1", "2", "3"])
                if decision_jugador2 == "1":
                    jugador2.atacar_rojo(jugador1)
                elif decision_jugador2 == "2":
                    jugador2.atacar_azul(jugador1)
                elif decision_jugador2 == "3":
                    jugador2.defender()
                    #jugador2.regenerar_energia_maldita()
        elif  isinstance(jugador2, PersonajeKamo):
            if jugador2.esta_vivo() and not jugador1.defendiendo:
                decision_jugador2 = random.choice(["1", "2", "3"])
                if decision_jugador2 == "1":
                    jugador2.atacar_golpe(jugador1)
                elif decision_jugador2 == "2":
                    jugador2.atacar_flechas_sangre(jugador1)
                elif decision_jugador2 == "3":
                    jugador2.defender()
        elif  isinstance(jugador2, PersonajeSukuna):
            if jugador2.esta_vivo() and not jugador1.defendiendo:
                decision_jugador2 = random.choice(["1", "2", "3"])
                if decision_jugador2 == "1":
                    jugador2.atacar_golpe(jugador1)
                elif decision_jugador2 == "2":
                    jugador2.atacar_patada(jugador1)
                elif decision_jugador2 == "3":
                    jugador2.defender()
            jugador1.reanudar_turno()

        if turnos_efectividad_infinito > 0:
            jugador1.efectividad_defensa = 0.2  
            turnos_efectividad_infinito -= 1
        else:
            jugador1.efectividad_defensa = 1  

    if jugador1.esta_vivo():
        jugador1.monedas += 1000
        print("Jugador 1 gana y obtiene 100 monedas adicionales.")
    else:
        print("Jugador 2 gana.")

    print("¡Fin del combate!")

    while True:
        opcion = mostrar_menu_compras(jugador1)
        if opcion == "1":
            if jugador1.monedas >= 10:
                print("¡Has comprado el Ataque Infinito!")
                jugador1.monedas -= 10
                jugador1.tiene_infinito = True
                turnos_efectividad_infinito = 3  
            else:
                print("¡No tienes suficientes monedas para comprar el Ataque Infinito!")
        elif opcion == "2":
            if jugador1.monedas >= 10:
                print("¡Has comprado el Ataque Púrpura!")
                jugador1.monedas -= 10
                jugador1.tiene_purpura = True
            else:
                print("¡No tienes suficientes monedas para comprar el Ataque Púrpura!")
        elif opcion == "3":
            if jugador1.monedas >= 100:
                print("¡Has comprado la Expansión de Dominio!")
                jugador1.monedas -= 100
                jugador1.tiene_expansion = True
                jugador2.vida = 0  
            else:
                print("¡No tienes suficientes monedas para comprar la Expansión de Dominio!")
        elif opcion == "4":
            menu_inicial()
        else:
            print("Opción inválida.")
            continue

        print(f"Monedas actuales: {jugador1.monedas}")
        continuar = input("¿Deseas seguir comprando? (s/n): ")
        if continuar.lower() != "s":
            break

menu_inicial()