# Programe en Python los autómatas obtenidos en el ejercicio 2 del Trabajo Práctico Nº 2.

class InitStateError(Exception):
    pass

class CharacterNotPresentError(Exception):
    pass

class EmptyInput(Exception):
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
        self.initSt      = estado_inicial
        self.endSts      = estados_finales
        self.blank       = caracter_vacio
        self.characters  = caracteres
        self.transitions = transiciones
        if self.initSt not in [key[0] for key in self.transitions.keys()]:
            raise InitStateError("El estado de inicio no esta incluido en las transiciones")

    def analyse(self, string: str, startPoint: int = 0) -> list:
        self.statesLog = {"Edo. Actual": [], "Caracter": [], "Simbolo": [], "Edo. Siguiente": []}
        stringList = list(string)
        state, index = self.initSt, startPoint
        if self.blank != None:
            stringList.append(self.blank)
            stringList.insert(0, self.blank)
            index += 1
        for iterations in range(0, len(stringList)*5):
            new_values = self.changeSt(state, stringList[index])
            state = new_values[0]
            stringList[index] = new_values[1]
            if stringList[index] == self.blank and str(state) in self.endSts:
                return [True, self.statesLog]
            index += 1 if new_values[2].lower() == 'r' else -1
            if (index+1 > len(stringList) or index < 0) and str(state) in self.endSts:
                return [True, self.statesLog]
        return [False, self.statesLog]

    def changeSt(self, st, char: str) -> tuple:
        for index, element in enumerate(list(self.characters.items())):
            if char in str(element[1]):
                self.statesLog["Simbolo"].append(element[0])
                break
            elif index == len(self.characters.keys())-1:
                raise ValueError(f"'{char}' no está entre los caracteres reconocidos", self.statesLog)
        self.statesLog["Edo. Actual"].append(st)
        self.statesLog["Caracter"].append(char)
        try:
            new_values = self.transitions[(st, element[0])]
            self.statesLog["Edo. Siguiente"].append(new_values[0])
            return new_values
        except KeyError:
            raise CharacterNotPresentError(f"'{char}' no esta presente en ninguna transición con el estado '{st}'", self.statesLog)
        

class MaquinaDeTuringApp():
    def __init__(self):
        pass

    def run(self):
        print("\n\nEsta aplicacion interpreta maquinas de turing y las ejecuta para cumplir su proposito.\n")
        app = ""
        while type(app) == str:
            user_input = input("Si quiere probar una de las maquinas ya cargadas oprima 'enter', de lo contrario, si desea introducir su propia maquina ingrese 'nueva':  ").replace(" ", "")
            if user_input.lower() == 'nueva':
                app = self.newTM()
            else:
                app = self.selectTM()
        while True:
            user_input = input("Ingrese una cadena a evaluar y presione 'enter':  ").replace(" ", "")
            try:
                if not user_input:
                    raise EmptyInput("No puedes ingresar una cadena vacía")
                user_input2 = input("Si desea comenzar a analizar la cadena desde un caracter en particular ingrese el numero, sino presione 'enter' y comenzara por la izquierda:  ").replace(" ", "")
                print(f"\n{user_input}\n")
                if user_input2.isdigit():
                    user_input2 = 0 if int(user_input2) > len(user_input) else user_input2
                    self.printer(app.analyse(user_input, int(user_input2)))
                else: 
                    self.printer(app.analyse(user_input))
            except (ValueError, CharacterNotPresentError, EmptyInput) as e:
                self.printer(e)
            
            user_input = input("Si desea ingresar una cadena nueva oprima el 'enter', sino ingrese 'no' para salir:  ").replace(" ", "")
            if user_input.lower() == 'no':
                break

    def newTM(self):
        estado_inicial = input("Ingrese el estado inicial y presione 'enter':  ").replace(" ", "")
        estados_finales = []
        print("Ahora ingrese el o los estados finales uno a uno, al terminar de ingresar el ultimo estado presione 'enter'")
        while True:
            print("Siguiente estado")
            user_input = input("Ingrese un estado y presione 'enter' (si ya no hay mas simplemente presione 'enter sin ingresar nada'):  ").replace(" ", "")
            if user_input == "":
                print(f"\n\n{estados_finales}\n\n")
                break
            estados_finales.append(user_input)
        caracter_vacio = input("Si utiliza el caracter vacio en algunas de las trasiciones ingreselo a continuacion y presione 'enter', si no lo utiliza no ingrese nada y simplemente presione 'enter':  ").replace(" ", "")
        caracteres = {}
        print("Ahora ingrese el o los caracteres uno a uno, al terminar de ingresar el ultimo caracter presione 'enter'")
        while True:
            print("Siguiente caracter")
            user_input = input("Ingrese un caracter y presione 'enter' (si ya no hay mas simplemente presione 'enter sin ingresar nada'):  ").replace(" ", "")
            if user_input == "":
                print(f"\n\n{caracteres}\n\n")
                break
            user_input2 = input("Si el caracter era una representacion, por ejemplo: 'num': 1,2,3,4, ingrese los caracteres que representa seguidos sin separadores, por ejemplo: 1234. Si el caracter no es una representacion simplemente presione 'enter' sin ingresar nada:  ").replace(" ", "")
            if user_input2 == "":
                caracteres[user_input] = user_input
            else: caracteres[user_input] = user_input2
        transiciones = {}
        print("Ahora ingrese las transiciones una a una, al terminar de ingresar la ultima transicion presione 'enter'")
        while True:
            print("Siguiente Transicion")
            print("La sintaxis de las transiciones es la siguiente: ('q1','a'): ('q2','b','r o l')")
            user_input = input("Ingrese el estado inicial y presione 'enter' (si ya no hay mas simplemente presione 'enter sin ingresar nada'):  ").replace(" ", "")
            if user_input == "":
                print(transiciones)
                break
            print("\n('q1',  )\n~~~~~~^^~")
            user_input2 = input("Ingrese el caracter que acompaña al estado y presione 'enter':  ").replace(" ", "")
            print("\n('q1','a'): (  ,)\n~~~~~~~~~~~~~^^~")
            user_input3 = input("Ingrese el estado nuevo y presione 'enter':  ").replace(" ", "")
            print("\n('q1','a'): ('q2',  ,)\n~~~~~~~~~~~~~~~~~~^^~")
            user_input4 = input("Ingrese el caracter que acompaña al estado nuevo y presione 'enter':  ").replace(" ", "")
            print("\n('q1','a'): ('q2','b',  )\n~~~~~~~~~~~~~~~~~~~~~~^^~")
            user_input5 = input("Ahora ingrese 'l' si es un desplazamiento a izquierda o 'r' si es a derecha y presione 'enter':  ").replace(" ", "")
            transiciones[(user_input, user_input2)] = (user_input3, user_input4, user_input5)
        try:
            app = MaquinaDeTuring(estado_inicial, estados_finales, caracter_vacio, caracteres, transiciones)
            return app
        except InitStateError as e:
            print("\n\n"+"ERROR!!\n"+e.args[0]+"\n\n")
            app = ""
            return app
        
    def selectTM(self):
        print(f"""Seleccione una de las siguientes opciones)
        1. Maquina A, (Automata ejercicio 2.a.) reconoce el lenguaje representado por esta regexp: {'x ( x | y ) *'} 
        2. Maquina B, (Automata ejercicio 2.b.) reconoce el lenguaje representado por esta regexp: {'(C | AC) *'} 
        3. Maquina C, (Automata ejercicio 2.c.) reconoce el lenguaje representado por esta regexp: {'(b | (b* a) *) a'} 
        4. Maquina D, reconoce el lenguaje de las operaciones aritmeticas (+,-,*,/) entre digitos""")
        while True:
            try:
                user_input = input("Ingrese el numero correspondiente a la maquina que desea utilizar:  ").replace(" ", "")
                if user_input == "1":
                    transiciones = {("q1", "x"): ("q2", "x", "R"), ("q2", "x"): ("q2", "x", "R"), ("q2", "y"): ("q2", "y", "R"), ("q2", "B"): ("q3", "B", "L")}
                    app = MaquinaDeTuring("q1", ["q3"], "B", {"x":"x", "y":"y", "B":"B"}, transiciones)
                    return app
                elif user_input == "2":
                    transiciones = {("q1", "A"): ("q2", "A", "R"), ("q1", "C"): ("q1", "C", "R"), ("q1", "B"): ("q3", "B", "L"), ("q2", "C"): ("q1", "C", "R")}
                    app = MaquinaDeTuring("q1", ["q3"], "B", {"A":"A", "C":"C", "B":"B"}, transiciones)
                    return app
                elif user_input == "3":
                    transiciones = {("q1", "a"): ("q5", "a", "R"),("q1", "b"): ("q2", "b", "R"),("q2", "a"): ("q5", "a", "R"),("q2", "b"): ("q3", "b", "R"),
                                    ("q3", "a"): ("q4", "a", "R"),("q3", "b"): ("q3", "b", "R"), ("q4", "a"): ("q5", "a", "R"),("q4", "b"): ("q3", "b", "R"),
                                    ("q5", "a"): ("q5", "a", "R"),("q5", "b"): ("q3", "b", "R"),("q5", "B"): ("q6", "B", "L")
                                    }
                    app = MaquinaDeTuring("q1", ["q6"], "B", {"a":"a", "b":"b", "B":"B"}, transiciones)
                    return app
                elif user_input == "4":
                    transiciones = {('q0', 'digito'): ('q1', 'digito', 'r'), ('q1', 'digito'): ('q1', 'digito', 'r'), ('q1', 'operador'): ('q2', 'operador', 'r'), 
                                    ('q2', 'digito'): ('q3', 'digito', 'r'), ('q3', 'operador'): ('q2', 'operador', 'r'), ('q3', 'digito'): ('q3', 'digito', 'r')}
                    app = MaquinaDeTuring("q1", ["q3"], None, {'operador': '+-*/', 'digito': '0123456789'}, transiciones)
                    return app
            except InitStateError as e:
                print("\n\n"+"ERROR!!\n"+e.args[0]+"\n\n")
                app = ""
                return app

    def printer(self, data):
        if type(data) == EmptyInput:
            print(data.args[0],'\n')
            return None

        exc_msg = ""
        if type(data) in [ValueError, CharacterNotPresentError]:
            data = list(data.args)
            exc_msg = "ERROR!!\n"+data[0]+"\n\n"
            data[0] = False
        print("+--------------+---------+-----------+---------------+")
        print("""|  Edo. Actual |Caracter |  Simbolo  |Edo. Siguiente |""")
        print("+--------------+---------+-----------+---------------+")
        for fase in range(0, len(data[1]["Edo. Siguiente"])):
            edo_actual = data[1]["Edo. Actual"][fase]
            caracter = data[1]["Caracter"][fase]
            simbolo = data[1]["Simbolo"][fase]
            edo_siguiente = data[1]["Edo. Siguiente"][fase]
            print(f"|      {edo_actual}      |    {caracter}    |  {simbolo:8} |      {edo_siguiente}       |")
            print("+--------------+---------+-----------+---------------+")
        if data[0]:
            print("""|                Cadena Valida :)                    |""")
            print("+--------------+---------+-----------+---------------+\n\n")
        else:
            print("""|              Cadena No Valida :(                   |""")
            print("+--------------+---------+-----------+---------------+\n\n")
        print(exc_msg, end="")

if __name__ == "__main__":
    app = MaquinaDeTuringApp()
    app.run()