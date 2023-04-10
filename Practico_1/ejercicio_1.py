# ejercicio_1
import random


class Ejercicio_1():

    def __init__(self):
        print('f')
        self.alphabet = ['a', 'b', 'c', 'd', '0', '1', '2', '3', '4']
        self.x = ""
        self.y = ""
        self.random_strings()

    def random_strings(self):
        for counter in range (0, random.randint(0,15)):
            self.x += random.choice(self.alphabet)
        for counter in range (0, random.randint(0,15)):
            self.y += random.choice(self.alphabet)
        print(self.x)
        print(self.y)
        
    def concatenar(self):
        return self.x + self.y

    def potencia(self, cadena, potencia):
        return cadena * potencia

if __name__ == '__main__':
    ejercicio_1 = Ejercicio_1()
