'''Implemente a través de Python analizador sintáctico predictivo no recursivo para la 
gramática: E→ E + E | E – E | E % E | ( E ) | id, y que funcione como calculadora, es 
decir, si la entrada es: 10+5-2, que muestre el resultado 13. % es la operación módulo o 
resto, por ejemplo 5%2 = 1, el resto de la división entre 5 y 2 es 1.'''

#E→ E + E | E – E | E % E | ( E ) | id
#E→ FE' E'→ +FE'|e F→ GF' F'→ -GF'|e G→ HG' G'→ %HG'|e H→ (E)|id
#id = num

class InvalidSyntax(Exception):
    pass

class InvalidCharacter(Exception):
    pass

class PredictiveSyntaxAnalyzer():
    def __init__(self):
        self.table = {
            "character": ["num", "+", "-", "%", "(", ")", "$"],
            "E": ["F E\'", "", "", "", "F E\'", "", ""],
            "E\'": ["", "+ F E\'", "", "", "", "e", "e"],
            "F": ["G F\'", "", "", "", "G F\'", "", ""],
            "F\'": ["", "e", "- G F\'", "", "", "e", "e"],
            "G": ["H G\'", "", "", "", "H G\'", "", ""],
            "G\'": ["", "e", "e", "% H G\'", "", "e", "e"],
            "H": ["num", "", "", "", "( E )", "", ""]}

    def analyze(self, string: str):
        string_list = list(str(string))
        if len(string_list) == 0:
            raise InvalidSyntax
        lifo = ["$", "E"]
        tree = {}
        for i, element in enumerate(string_list):
            if element.isdigit():
                if string_list[i-1].isdigit():
                    continue
                element = "num"
            while True:
                if lifo[-1] in ["num", "+", "-", "%", "(", ")"]:
                    lifo.pop()
                    break
                elif lifo[-1] == "$":
                    return True, tree
                non_ter = lifo.pop()
                char_list = self.findTableValue(non_ter, element)
                if non_ter not in tree.keys():
                    tree[non_ter] = set(char_list)
                val = set(char_list)
                tree[non_ter].union(val)
                lifo.extend(char_list)
                if lifo[-1] == "e":
                    lifo.pop()
                elif lifo[-1] == "":
                    raise InvalidSyntax(f"Invalid Syntax: '{string_list[i-1]+string_list[i]}'")
    def findTableValue(self, lifo: str, char: str) -> list:
        try:
            index = self.table.get("character").index(char)
            return self.table.get(lifo)[index].split(" ")[::-1]
        except ValueError:
            raise InvalidCharacter(f"'{char}' is not in the list of recognized characters")


class Calculator(PredictiveSyntaxAnalyzer):
    def __init__(self):
        super().__init__()
    
    def calculate(self, string: str):
        try:
            tree = self.analyze(string)[1]
            return(f'La sintaxis es correcta, el resultado de la operacion es: {eval(string.strip("$"))}'), tree
        except Exception as e:
            return(e)

class UserInterface(Calculator):
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        while True:
            self.ask_input()
            user_input = input("Desea calcular otra expresion y/n ")
            if user_input in ["y", "Y"]:
                continue
            elif user_input in ["n", "N"]:
                exit()

    def ask_input(self):
        string = input("Ingrese una expresion a calcular ")+"$"
        resol, tree = self.calculate(string)
        print(resol)
        print(tree)



if __name__ == "__main__":
    app = UserInterface()
    app.run()