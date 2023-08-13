def emit(code):
    print(code)

# Função para simular o método emitjumps
def emitjumps(test, t, f):
    if t != 0 and f != 0:
        emit("if " + test + " goto L" + str(t))
        emit("goto L" + str(f))
    elif t != 0:
        emit("if " + test + " goto L" + str(t))
    elif f != 0:
        emit("iffalse " + test + " goto L" + str(f))
    else:
        pass  # Nada, pois tanto t quanto f caem diretamente

# Função que simula o comportamento da classe Expr
def create_expr(tok, p):
    op = tok
    type_ = p

    def gen():
        return create_expr(op, reduce(expr1), reduce(expr2))

    def reduce(expression):
        return create_expr(op, reduce(expr1), reduce(expr2))

    def jumping(t, f):
        emitjumps(str(op), t, f)

    def get_str():
        return str(op)

    return {
        'gen': gen,
        'reduce': reduce,
        'jumping': jumping,
        'get_str': get_str
    }
