# Arq Access.py
import Word, Tag
import Type
import Op
import Expr

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
