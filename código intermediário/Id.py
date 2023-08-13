from lexer import Word
from symbols import Type
from Expr import Expr  

class Id(Expr):
    def __init__(self, id_token, p, b):
        super().__init__(id_token, p)
        self.offset = b
