import random
from datetime import datetime, date


def  numero_aleatorio():
    numero_random = random.randint(1,50)
    return numero_random


def numero_elegir():
        while True:

            try:
                numero = int(input("Ingrese un numero: "))

                while 0 >= numero or numero >= 100:
                    numero = int(input("Ingrese un numero entre el 1 y el 99: "))

                break

            except ValueError:
                print('Error, el valor no pude ser tipo '
                      'string o flotante, ingrese un entero')
        return numero


def funcion_decoradora(funcion_elegir):
    def funcion():
        print('Bienvenido a este juego llamado: Adivina el número!')
        resultado = funcion_elegir()
        print(resultado)
        print('Juego terminado, gracias por jugar!')
    return funcion


@funcion_decoradora
def adivina():
    num_aleatorio = numero_aleatorio()
    num = numero_elegir()
    while num != num_aleatorio:
        if num_aleatorio > num:
            print('El numero aleatorio es mayor que el numero elegido.')
            num = numero_elegir()

        elif num_aleatorio < num:
            print('El número aleatorio es menor que el numero elegido.')
            num = numero_elegir()

    fecha = date.today()
    hora = datetime.now()
    dia = fecha.day
    mes = fecha.month
    horas = hora.hour
    minutos = hora.minute
    return f'Has ganado! \nFecha y hora de acertado: {dia}/{mes} - {horas}:{minutos}'
