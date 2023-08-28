# Arq Access.py
from lexer import Word, Tag
from symbols import Type
from op import Op
from expr import Expr
from emit import emitjumps

def create_access(a, i, p):
    super(Word("[]", Tag.INDEX), p)  # p is element type after flattening the array
    array = a
    index = i

def gen_access():
    return Access(array, index["reduce"](), type)

def jumping_access(t, f):
    emitjumps(reduce()["toString"](), t, f)

def to_string_access():
    return array["toString"]() + " [ " + index["toString"]() + " ]"
