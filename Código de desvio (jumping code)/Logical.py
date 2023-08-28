# Arq Logical.py
import Token
import Type
import Expr, Temp

def create_logical(tok, x1, x2):
    super(tok, None)  # null type to start
    expr1 = x1
    expr2 = x2
    type = check(expr1["type"], expr2["type"])
    if type is None:
        error("erro de tipo")

def check_logical(p1, p2):
    if p1 == Type.BOOL and p2 == Type.BOOL:
        return Type.BOOL
    else:
        return None

def gen_logical():
    f = newlabel()
    a = newlabel()
    temp = Temp(type)
    jumping(0, f)
    emit(temp["toString"]() + " = true")
    emit("goto L" + str(a))
    emitlabel(f)
    emit(temp["toString"]() + " = false")
    emitlabel(a)
    return temp

def to_string_logical():
    return expr1["toString"]() + " " + op["toString"]() + " " + expr2["toString"]()
