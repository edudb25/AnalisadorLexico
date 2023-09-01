#Arq Else.py
import Type#,newlabel
import Stmt
import Expr


def create_else_stmt(x, s1, s2):
    if x["type"] != Type.BOOL:
        x["error"]("boolean required in if")

    label1 = newlabel()  # label1 para stmt1
    label2 = newlabel()  # label2 para stmt2
    jumping(x, 0, label2)  # fall through to stmt1 on true
    emitlabel(label1)
    gen(s1, label1, s2["a"])
    emit("goto L" + str(s2["a"]))
    emitlabel(label2)
    gen(s2, label2, s2["a"])
