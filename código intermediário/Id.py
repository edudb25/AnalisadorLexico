from lexer import Word
from symbols import Type

def create_id(id_token, p, b):
    offset = b
    
    def expr():
        return {
            "op": id_token,
            "type": p,
            "offset": offset,
            "gen": gen,
            "reduce": reduce,
            "__str__": __str__
        }
    
    def gen():
        return expr()
    
    def reduce():
        return expr()
    
    def __str__():
        return str(id_token)
    
    return expr()

