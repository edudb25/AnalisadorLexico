from symbols import Type
from Op import Op  # Certifique-se de importar a classe Op se não estiver incluída no arquivo

def Arith(tok, x1, x2):
    expr1 = x1
    expr2 = x2
    op = tok.value
    type_ = Type.max(x1['type'], x2['type'])
    
    if type_ is None:
        error("type error")

    def gen():
        return Arith(op, reduce(expr1), reduce(expr2))

    def __str__():
        return str(expr1) + " " + str(op) + " " + str(expr2)

    return {
        'expr1': expr1,
        'expr2': expr2,
        'op': op,
        'type': type_,
        'gen': gen,
        '__str__': __str__
    }

def reduce(expression):
    # Implemente a lógica para reduzir a expressão
    pass

def error(message):
    print("Error:", message)

# Exemplo de uso
tok = {'value': '+'}
x1 = {'type': Type(), 'reduce': lambda: 5}
x2 = {'type': Type(), 'reduce': lambda: 3}
arith_expr = Arith(tok, x1, x2)
print(arith_expr['gen']())
print(arith_expr['__str__']())
