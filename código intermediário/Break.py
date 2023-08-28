# Arq Break.py
from stmt import Stmt
from emit import emit, error

stmt = None

def create_break():
    global stmt

    if Stmt.Enclosing is None:
        error("break não associado a um bloco")
    stmt = Stmt.Enclosing

def gen_break(b, a):
    emit("goto L" + str(stmt["after"]))
