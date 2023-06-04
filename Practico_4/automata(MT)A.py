# Programe en Python los autómatas obtenidos en el ejercicio 2 del Trabajo Práctico Nº 2.
# x ( x | y ) *
# Q = {q1, q2, q3}
# Ʃ = {x, y}
# Г = {x, y, B}
# s = q1
# F = {q3}
# δ dado por: 	δ(q1, x) = (q2, x, R)
# 		δ(q2, x) = (q2, x, R)
# 		δ(q2, y) = (q2, y, R)
# 		δ(q2, B) = (q3, B, R)

import re

class InitStateError(Exception):
    pass

class CharacterNotPresentError(InitStateError):
    pass

class MaquinaDeTuring():
    def __init__(self, 
                 estado_inicial: str | int, 
                 estados_finales: list,
                 caracter_vacio: str | None,
                 caracteres: dict, 
                 transiciones: dict
                ):
        """
        Formato requerido para parametros:\n
        caracteres: {"a":"a","operador":"+-*/","num": "123456789"}\n
        transiciones: {("q1","a"): ("q2","b","r | l")}
        """
        self.initSt = estado_inicial
        self.endSts = estados_finales
        self.blank = caracter_vacio
        self.characters = caracteres
        self.transitions = transiciones
        if self.initSt not in [key[0] for key in self.transitions.keys()]:
            raise InitStateError("El estado de inicio no esta incluido en las transiciones")
        self.statesLog = {"Edo. Actual": [], "Caracter": [], "Simbolo": [], "Edo. Siguiente": []}

    def analyse(self, string: str, startPoint: int = 0) -> list:
        stringList = list(string)
        state, index = self.initSt, startPoint
        if self.blank != None:
            stringList.append(self.blank)
            stringList.insert(0, self.blank)
            state[1] += 1
        for iterations in range(0, len(stringList)*5):
            new_values = self.changeSt(state, stringList[index])
            state = new_values[0]
            stringList[index] = new_values[1]
            index += 1 if new_values[2] in ["r","R"] else -1
            if (index+1 > len(stringList) or index < 0) and str(state) in self.endSts:
                return [True, self.statesLog]
            elif stringList[index] == self.blank and str(state) in self.endSts:
                return [True, self.statesLog]
        return [False, self.statesLog]

    def changeSt(self, st, char: str) -> tuple:
        for index, key, value in enumerate(self.characters.items()):
            if char in str(value):
                self.statesLog["Simbolo"].append(key)
                break
            elif index == len(self.characters.keys()-1):
                raise ValueError(f"'{char}' no está entre los caracteres reconocidos", self.statesLog)
        self.statesLog["Edo. Actual"].append(st)
        self.statesLog["Caracter"].append(char)
        try:
            new_values = self.transitions[(st, char)]
            self.statesLog["Edo. Siguiente"].append(new_values[0])
            return new_values
        except KeyError:
            raise CharacterNotPresentError(f"'{char}' no esta presente en ninguna transición", self.statesLog)
        

class MaquinaDeTuringApp():
    def __init__(self):
        pass

    def run(self):
        print("Esta aplicacion interpreta maquinas de turing y las ejecuta para cumplir su proposito")
        while type(app) == str:
            user_input = input("Si quiere probar una de las maquinas ya cargadas oprima 'enter', de lo contrario, si desea introducir su propia maquina ingrese 'nueva'  ")
            if user_input in ["nueva", "Nueva", "NUEVA"]:
                app = self.newTM()
            else:
                app = self.selectTM()
        while True:
            user_input = input("Ingrese una cadena a evaluar y presione 'enter':  ")
            user_input2 = input("Si desea comenzar a analizar la cadena desde un caracter en particular ingrese el numero, sino presione 'enter' y comenzara por la izquierda:  ")
            print("\n"+user_input+"\n")
            try:
                if user_input2 != "" and user_input2.isdigit():
                    self.printer(app.analyse(user_input, user_input2))
                else: 
                    self.printer(result = app.analyse(user_input))
            except Exception as e:
                self.printer(e.args)
            user_input = input("Si desea ingresar una cadena nueva oprima el 'enter', sino ingrese 'no' para salir:  ")
            if user_input in ["no", "No", "NO"]:
                break


    def newTM(self):
        estado_inicial = input("Ingrese el estado inicial y presione 'enter':  ").replace(" ", "")
        estados_finales = []
        print("Ahora ingrese el o los estados finales uno a uno, al terminar de ingresar el ultimo estado presione 'enter'")
        while True:
            print("Siguiente estado")
            user_input = input("Ingrese un estado y presione 'enter' (si ya no hay mas simplemente presione 'enter sin ingresar nada'):  ").replace(" ", "")
            estados_finales.append(user_input)
            if user_input == "":
                print(f"\n\n{estados_finales}\n\n")
                break
        caracter_vacio = input("Si utiliza el caracter vacio en algunas de las trasiciones ingreselo a continuacion y presione 'enter', si no lo utiliza no ingrese nada y simplemente presione 'enter':  ").replace(" ", "")
        caracteres = {}
        print("Ahora ingrese el o los caracteres uno a uno, al terminar de ingresar el ultimo caracter presione 'enter'")
        while True:
            print("Siguiente caracter")
            user_input = input("Ingrese un caracter y presione 'enter' (si ya no hay mas simplemente presione 'enter sin ingresar nada'):  ").replace(" ", "")
            user_input2 = input("Si el caracter era una representacion, por ejemplo: 'num': 1,2,3,4, ingrese los caracteres que representa seguidos sin separadores, por ejemplo: 1234. Si el caracter no es una representacion simplemente presione 'enter' sin ingresar nada:  ").replace(" ", "")
            if user_input2 == "":
                caracteres[user_input] = user_input
            else: caracteres[user_input] = user_input2
            if user_input == "":
                print(f"\n\n{caracteres}\n\n")
                break
        transiciones = {}
        print("Ahora ingrese las transiciones una a una, al terminar de ingresar la ultima transicion presione 'enter'")
        while True:
            print("Siguiente Transicion")
            print("La sintaxis de las transiciones es la siguiente: ('q1','a'): ('q2','b','r o l')")
            user_input = input("Ingrese el estado inicial y presione 'enter' (si ya no hay mas simplemente presione 'enter sin ingresar nada'):  ").replace(" ", "")
            print("\n('q1',  )\n~~~~~~^^~")
            user_input2 = input("Ingrese el caracter que acompaña al estado y presione 'enter':  ").replace(" ", "")
            print("\n('q1','a'): (  ,)\n~~~~~~~~~~~~~^^~")
            user_input3 = input("Ingrese el estado nuevo y presione 'enter':  ").replace(" ", "")
            print("\n('q1','a'): ('q2',  ,)\n~~~~~~~~~~~~~~~~~~^^~")
            user_input4 = input("Ingrese el caracter que acompaña al estado nuevo y presione 'enter':  ").replace(" ", "")
            print("\n('q1','a'): ('q2','b',  )\n~~~~~~~~~~~~~~~~~~~~~~^^~")
            user_input5 = input("Ahora ingrese 'l' si es un desplazamiento a izquierda o 'r' si es a derecha y presione 'enter':  ").replace(" ", "")
            transiciones[(user_input, user_input2)] = (user_input3, user_input4, user_input5)
            if user_input == "":
                print(caracteres)
                break
        try:
            app = MaquinaDeTuring(estado_inicial, estados_finales, caracter_vacio, caracteres, transiciones)
            return app
        except InitStateError as e:
            print("\n\n"+"ERROR!!\n"+e.args[0]+"\n\n")
            app = ""
            return app
        
    def selectTM(self):
        print("Seleccione una de las siguientes opciones")
        print("1) Maquina A, reconoce el lenguaje representado por esta expresion regular: 'x ( x | y ) *' (Automata ejercicio 2)a)")
        print("2) Maquina B, reconoce el lenguaje representado por esta expresion regular: '(C | AC) *' (Automata ejercicio 2)b)")
        print("3) Maquina C, reconoce el lenguaje representado por esta expresion regular: '(b | (b* a) *) a' (Automata ejercicio 2)c)")
        while True:
            try:
                user_input = input("Ingrese el numero correspondiente a la maquina que desea utilizar:  ").replace(" ", "")
                if user_input == "1":
                    transiciones = {("q1", "x"): ("q2", "x", "R"), ("q2", "x"): ("q2", "x", "R"), ("q2", "y"): ("q2", "y", "R"), ("q2", "B"): ("q3", "B", "R")}
                    app = MaquinaDeTuring("q1", ["q3"], "B", {"x":"x", "y":"y", "B":"B"}, transiciones)
                    return app
                elif user_input == "2":
                    transiciones = {("q1", "A"): ("q2", "A", "R"), ("q1", "C"): ("q1", "C", "R"), ("q1", "B"): ("q3", "B", "R"), ("q2", "C"): ("q1", "C", "R")}
                    app = MaquinaDeTuring("q1", ["q3"], "B", {"A":"A", "C":"C", "B":"B"}, transiciones)
                    return app
                elif user_input == "3":
                    transiciones = {("q1", "a"): ("q5", "a", "R"),("q1", "b"): ("q2", "b", "R"),("q2", "a"): ("q5", "a", "R"),("q2", "b"): ("q3", "b", "R"),
                                    ("q3", "a"): ("q4", "a", "R"),("q3", "b"): ("q3", "b", "R"), ("q4", "a"): ("q5", "a", "R"),("q4", "b"): ("q3", "b", "R"),
                                    ("q5", "a"): ("q5", "a", "R"),("q5", "b"): ("q3", "b", "R"),("q5", "B"): ("q6", "B", "R")
                                    }
                    app = MaquinaDeTuring("q1", ["q6"], "B", {"a":"a", "b":"b", "B":"B"}, transiciones)
                    return app
            except InitStateError as e:
                print("\n\n"+"ERROR!!\n"+e.args[0]+"\n\n")
                app = ""
                return app

    def printer(self, data):
        if type(data) == Exception:
            exc_msg = data[0]
            data[0] = False
        print("+--------------+---------+-----------+---------------+")
        print("""|  Edo. Actual |Caracter |  Simbolo  |Edo. Siguiente |""")
        print("+--------------+---------+-----------+---------------+")
        for fase in len(data[1]["Edo. Actual"]):
            print("|     ",data[1]["Edo. Actual"],"      |  ",data[1]["Caracter"],"    |",data[1]["Simbolo"]," |     ",data[1]["Edo. Siguiente"],"       |")
            print("+--------------+---------+-----------+---------------+")
        if data[0]:
            print("""|                Cadena Valida :)                    |""")
        else:
            print("""|              Cadena No Valida :(                   |""")
        if type(data) == Exception:
            print("ERROR!!\n"+exc_msg)