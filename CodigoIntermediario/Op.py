# Funções para simular Token e Type
def create_token(value):
    return {'value': value}

def create_type():
    return {}

# Função que simula o comportamento da classe Op
def create_op(tok, p):
    op = tok
    type_ = p

    def reduce(expression):
        x = gen()
        t = Temp(type_)
        emit(str(t) + " = " + str(x))
        return t

    return {
        'reduce': reduce
    }

# Função que simula o comportamento da função Temp
def Temp(type_):
    return "Temp_" + str(type_)

