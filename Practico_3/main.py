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
        for element in string_list:
            try:
                element = int(element)
                element = "num"
            except ValueError:
                pass
            while element != lifo[-1]:
                char_list = self.findTableValue(lifo[-1], element)
                if char_list[0] == "e":
                    lifo.pop()
                elif char_list[0] == "":
                    raise InvalidSyntax
                else:
                    lifo.pop()
                    lifo.extend(char_list)
            lifo.pop()
        return True

    def findTableValue(self, lifo: str, char: str) -> list:
        try:
            index = self.table.get("character").index(char)
            return self.table.get(lifo)[index].split(" ")[::-1]
        except ValueError:
            raise InvalidCharacter(f"{char} is not in the list of recognized characters")


class Calculator(PredictiveSyntaxAnalyzer):
    def __init__(self):
        super.__init__(self)
    
    def calculate(self):
        pass