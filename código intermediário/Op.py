from lexer import Token
from symbols import Type
from Expr import Expr, Temp 
class Op(Expr):
    def __init__(self, tok, p):
        super().__init__(tok, p)

    def reduce(self):
        x = self.gen()
        t = Temp(self.type)
        self.emit(str(t) + " = " + str(x))
        return t
