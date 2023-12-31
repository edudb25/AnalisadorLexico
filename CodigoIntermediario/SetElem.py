# Arq SetElem.py
import Id
import Type, Array
import Stmt
import Expr, Access

def create_set_elem(x, y):
    global array, index, expr
    array = x["array"]
    index = x["index"]
    expr = y

    if check(x["type"], y["type"]) is None:
        error("erro de tipo")

def check(p1, p2):
    if isinstance(p1, Array) or isinstance(p2, Array):
        return None
    elif p1 == p2:
        return p2
    elif Type.numeric(p1) and Type.numeric(p2):
        return p2
    else:
        return None

def gen_set_elem(b, a):
    s1 = index["reduce"]()["toString"]()
    s2 = expr["reduce"]()["toString"]()
    emit(array["toString"]() + " [ " + s1 + " ] = " + s2)
