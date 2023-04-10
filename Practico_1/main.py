"""Implementar mediante el lenguaje Python un autómata que reconozca números con o sin signo y en formato exponencial.
Usando una matriz de transición. Para implementar la matriz de transición en Python, se pueden utilizar listas.
[[2,1,1,'','',''],
[2,'','','','' ,'']
['acepta', 'acepta', 'acepta', 'acepta', 'acepta','acepta']]"""
import time
T = [
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
    print(f'Analizando la cadena {cadena}')
    cadena = cadena
    estado_actual = 0
    columna = 0
    pos = 0
    while True:
        if [pos].isdigit():
            columna = 0
        elif cadena[pos] == '+':
            columna = 1
        elif cadena[pos] == '-':
            columna = 2
        elif cadena[pos] == '.':
            columna = 3
        elif cadena[pos].lower() == 'e':
            columna = 4
        elif cadena[pos] == '$':
            columna = 5
        else:
            return False
        print(f'Estado actual: {estado_actual}\n Columna: {columna}\n Letra{cadena[pos]}')
        time.sleep(0.5)
        estado_actual = T[estado_actual][columna]
        if estado_actual == ' ':
            return False
        if estado_actual == '8':
            return True
        pos += 1
if __name__ == '__main__':
    print(automata('123$'))