# Arq Do.py
import Type#, newlabel
import Stmt
import Expr

expr = None
stmt = None

def init_do(s, x):
    global expr, stmt
    expr = x
    stmt = s

    if x["type"] != Type.BOOL:
        x["error"]("booleano necessário no do")

def gen_do(b, a):
    global expr, stmt
    after = a
    label = newlabel()  # Rótulo para expr
    stmt.gen(b, label)
    emitlabel(label)
    expr.jumping(b, 0)
