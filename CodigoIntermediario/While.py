# Arq While.py
import Type
from Node import newlabel, emitlabel, emit
import Stmt
from Expr import expr

expr = None
stmt = None

def init_while(x, s):
    global expr, stmt
    expr = x
    stmt = s

    if x["type"] != Type.BOOL:
        x["error"]("booleano necessário no while")

def gen_while(b, a):
    global expr, stmt
    after = a  # Salvar rótulo a
    jumping(expr, 0, a)
    label = newlabel()  # Rótulo para stmt
    emitlabel(label)
    gen(stmt, label, b)
    emit("goto L" + str(b))
