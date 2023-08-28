# Arq If.py
import Type #, newlabel
import Stmt
import Expr

def create_if_stmt(x, s):
    if x["type"] != Type.BOOL:
        x["error"]("boolean required in if")

    label = newlabel()  # label for the code for stmt
    jumping(x, 0, s["a"])  # fall through on true, goto a on false
    emitlabel(label)
    gen(s, label, s["a"])
