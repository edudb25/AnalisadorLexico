from lexer import Word
from symbols import Type
from Expr import Expr  
class Temp(Expr):
    count = 0

    def __init__(self, p):
        super().__init__(Word.temp, p)
        self.number = Temp.count
        Temp.count += 1

    def __str__(self):
        return "t" + str(self.number)
