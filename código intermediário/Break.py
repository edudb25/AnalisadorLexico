# Arq Break.py
import Stmt

stmt = None

def create_break():
    global stmt

    if Stmt.Enclosing is None:
        error("break não associado a um bloco")
    stmt = Stmt.Enclosing

def gen_break(b, a):
    emit("goto L" + str(stmt["after"]))
