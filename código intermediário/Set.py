# Arq Set.py
import Id
import Type
import Stmt
import Expr


def create_set_stmt(i, x):
    id = i
    expr = x

    if check(id["type"], expr["type"]) is None:
        error("erro de tipo")

def check(p1, p2):
    if Type.numeric(p1) and Type.numeric(p2):
        return p2
    elif p1 == Type.BOOL and p2 == Type.BOOL:
        return p2
    else:
        return None

def gen_set(b, a):
    emit(id["toString"]() + " = " + expr["gen"]()["toString"]())
