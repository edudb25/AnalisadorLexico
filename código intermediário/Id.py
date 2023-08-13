# Simulando a classe Word
def create_word(value, token_type):
    return {
        'value': value,
        'token_type': token_type
    }

# Simulando a classe Type (sem atributos)
type_instance = {}

# Função para simular o método emit
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

# Função que simula o comportamento da classe Id
def create_id(id_value, token_type, p, b):
    op = create_word(id_value, token_type)
    type_ = p
    offset = b

    def gen():
        return create_id(op['value'], reduce(expr1), reduce(expr2), p, b)

    def reduce(expression):
        return create_id(op['value'], reduce(expr1), reduce(expr2), p, b)

    def jumping(t, f):
        emitjumps(str(op['value']), t, f)

    return {
        'gen': gen,
        'reduce': reduce,
        'jumping': jumping
    }

