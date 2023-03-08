import random

def play():
    persona = input("elegir opcion. '1' piedra, '2' papel, '3'tijera: ")

    opciones = ['1', '2', '3']
    pc = random.choice(opciones)

    if persona == pc:
        return "usted y la pc eligieron {}".format(pc)

    if ganador(persona, pc):
        return "usted eligió {} y la pc {}. ganó".format(persona, pc)

    return "usted escogió {} y la pc {}. perdió".format(persona, pc)

def ganador (jugador1, jugador2):
    if (jugador1 == '1' and jugador2 == '3') or (jugador1 == '2' and jugador2 == '1') or (jugador1 == '3' and jugador2 == '2'):
        return ganador 
print(play())


