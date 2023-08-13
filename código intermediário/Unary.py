from lexer import Token
from symbols import Type
from Op import Op 
class Unary(Op):
    def __init__(self, tok, x):
        super().__init__(tok, None)
        self.expr = x
        self.type = Type.max(Type.Int, x.type)
        if self.type is None:
            self.error("type error")

    def gen(self):
        return Unary(self.op, self.expr.reduce())

    def __str__(self):
        return str(self.op) + " " + str(self.expr)
