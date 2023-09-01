# Arq Seq.py
import Stmt

def create_seq(s1, s2):
    stmt1 = s1
    stmt2 = s2

def gen_seq(b, a):
    if stmt1 == Stmt.Null:
        stmt2.gen(b, a)
    elif stmt2 == Stmt.Null:
        stmt1.gen(b, a)
    else:
        label = newlabel()
        stmt1.gen(b, label)
        emitlabel(label)
        stmt2.gen(label, a)
