# Arq Rel.py
import Token
import Type, Array
import Expr, Logical

def create_rel(tok, x1, x2):
    super(tok, x1, x2)

def check_rel(p1, p2):
    if isinstance(p1, Array) or isinstance(p2, Array):
        return None
    elif p1 == p2:
        return Type.BOOL
    else:
        return None

def jumping_rel(t, f):
    a = expr1["reduce"]()
    b = expr2["reduce"]()

    test = a["toString"]() + " " + op["toString"]() + " " + b["toString"]()
    emitjumps(test, t, f)
