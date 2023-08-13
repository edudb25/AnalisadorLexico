from lexer import Token
from symbols import Type
from Node import Node  # Certifique-se de importar a classe Node se ela não estiver incluída no arquivo

class Expr(Node):
    def __init__(self, tok, p):
        self.op = tok
        self.type = p

    def gen(self):
        return self

    def reduce(self):
        return self

    def jumping(self, t, f):
        self.emitjumps(str(self), t, f)

    def emitjumps(self, test, t, f):
        if t != 0 and f != 0:
            self.emit("if " + test + " goto L" + str(t))
            self.emit("goto L" + str(f))
        elif t != 0:
            self.emit("if " + test + " goto L" + str(t))
        elif f != 0:
            self.emit("iffalse " + test + " goto L" + str(f))
        else:
            pass  # Nada, pois tanto t quanto f caem diretamente

    def __str__(self):
        return str(self.op)
