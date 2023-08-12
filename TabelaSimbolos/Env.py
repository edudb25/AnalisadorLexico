import Lexer
from Inter import Id

# File: Env.py
def create_env(n):
    table = {}
    prev = n

    def put(w, i):
        nonlocal table
        table[w] = i

    def get(w):
        nonlocal table, prev
        e = create_env
        while e:
            found = e.table.get(w)
            if found:
                return found
            e = e.prev
        return None

    return {"put": put, "get": get}

'''from lexer import Token
from inter import Id'''