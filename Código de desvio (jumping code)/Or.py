# Arq Or.py
import Token
import Type
import Expr, Logical

def create_or(tok, x1, x2):
    super(tok, x1, x2)

def jumping_or(t, f):
    label = t if t != 0 else newlabel()
    expr1.jumping(label, 0)
    expr2.jumping(t, f)
    if t == 0:
        emitlabel(label)
