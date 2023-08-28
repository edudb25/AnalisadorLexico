# Arq And.py
from lexer import Token
from symbols import Type
from expr import Expr, Logical
from emit import emit, emitlabel, newlabel

def create_and(tok, x1, x2):
    super(tok, x1, x2)

def jumping_and(t, f):
    label = f if f != 0 else newlabel()
    expr1.jumping(0, label)
    expr2.jumping(t, f)
    if f == 0:
        emitlabel(label)

