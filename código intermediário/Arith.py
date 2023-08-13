from lexer import Token
from symbols import Type
from Op import Op  # Certifique-se de importar a classe Op se não estiver incluída no arquivo

class Arith(Op):
    def __init__(self, tok, x1, x2):
        super().__init__(tok, None)
        self.expr1 = x1
        self.expr2 = x2
        self.type = Type.max(x1.type, x2.type)
        if self.type is None:
            self.error("type error")

    def gen(self):
        return Arith(self.op, self.expr1.reduce(), self.expr2.reduce())

    def __str__(self):
        return str(self.expr1) + " " + str(self.op) + " " + str(self.expr2)
