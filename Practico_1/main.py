"""Implementar mediante el lenguaje Python un autómata que reconozca números con o sin signo y en formato exponencial.
Usando una matriz de transición. Para implementar la matriz de transición en Python, se pueden utilizar listas.
[[2,1,1,'','',''],
[2,'','','','' ,'']
['acepta', 'acepta', 'acepta', 'acepta', 'acepta','acepta']]"""

import time

matriz = [
    ['2', '1', '1', ' ', ' ',' '],
    ['2', ' ', ' ', ' ', ' ',' '],
    ['2', ' ', ' ', '3', '5','8'],
    ['4', ' ', ' ', ' ', ' ',' '],
    ['4', ' ', ' ', ' ', '5','8'],
    ['7', '6', '6', ' ', ' ',' '],
    ['7', ' ', ' ', ' ', ' ',' '],
    ['7', ' ', ' ', ' ', ' ','8'],
    ['acepta','acepta','acepta','acepta','acepta','acepta','acepta','acepta']
]

def automata(cadena):
    cadena = str(cadena)
    estado_actual = 0
    columna = 0
    caracteres = ['+', '-', '.', 'e', '$']
    for pos in range(0, len(cadena)+1):
        try:
            if cadena[pos].isdigit():
                columna = 0
            elif cadena[pos] in caracteres:
                columna = caracteres.index(cadena[pos])+1
            else: 
                raise ValueError
        except (IndexError, ValueError) as e:
            return False, f'{cadena} no es un número identificable'
    
        #print(f'Estado actual: {estado_actual}\n Columna: {columna}\n Caracter{cadena[pos]}')
        estado_actual = matriz[int(estado_actual)][columna]
        if estado_actual == ' ':
            return False, f'{cadena} no es un número identificable'
        if estado_actual == '8':
            return True, f'{cadena} es un número'


if __name__ == '__main__':
    numeros_test = ['1ab2$','12.e4$','a1$','1e12e0$','++$','e12$','120379$', '+120379$', '-120379$', '120379e14$', '120379e-14$', '120379e+14$', '12.0379$', '1203.79e-14$']
    for number in numeros_test:
        print(automata(number)[1])