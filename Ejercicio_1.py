import datetime


def funcion_decoradora(funcion_decorar):
    def funcion(*args, **kwargs):
        tiempo_inicial = datetime.datetime.now()
        resultado = funcion_decorar(*args, **kwargs)
        print(f'El diccionario de la persona es: {resultado}')
        tiempo_final = datetime.datetime.now()
        print(f'Tiempo de ejecucion: {tiempo_final - tiempo_inicial}')
    return funcion


class Persona:
    def __init__(self):
        self.__nombre = input('Ingresa tu nombre: ')
        self.edad = int(input('Ingresa tu edad: '))
        self.ciudad = input('Ingresa tu ciudad: ')


    def datos(self):
        print(f'Sus datos son los siguientes: '
              f'Usted se llama {self.__nombre}, '
              f'tiene {self.edad} años y '
              f'vive en {self.ciudad}')


    def obtener_nombre(self):
        return self.__nombre


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input('Ingresa tu sueldo: '))
        self.impuestos = self.impuesto()

    def impuesto(self):
        if self.sueldo > 5500:
            impuestos = 0.09 * self.sueldo
            print(f'Usted tiene que pagar un impuesto de {impuestos} soles')
            return impuestos
        else:
            impuestos = 0
            print('Usted no tiene que pagar impuestos.')
            return impuestos


    @funcion_decoradora
    def manejo_diccionario(self):

        dicc = {'nombre': self.obtener_nombre(),
                'edad': self.edad,
                'sueldo': self.sueldo,
                'impuestos': self.impuestos}

        return dicc


persona1 = Empleado()
persona1.datos()
persona1.manejo_diccionario()

persona2 = Empleado()
persona2.datos()
persona2.manejo_diccionario()
