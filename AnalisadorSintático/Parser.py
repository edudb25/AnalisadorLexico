import Lexer
import Tag
import Type
import Word
import Stmt
import While
import Id
import Seq
import Array
import Do
import Lexer
import If
import Else
import Break
import Or
import And
import Not
import Rel
import Arith
import Set
import SetElem
import Constant
import Token
import Access
import Unary

from Node import emitlabel

top = None
used = 0

def move():
    global look
    look = lex.scan()

def error(s):
    raise Exception(f"near line {lex.line}: {s}")

def match(t):
    global look
    if look.tag == t:
        move()
    else:
        error("syntax error")

def program():
    s = block()
    begin = s.newlabel()
    after = s.newlabel()
    emitlabel(begin)
    gen(begin, after)
    emitlabel(after)

def block():
    match('{')
    savedEnv = top
    top = dict()
    decls()
    s = stmts()
    match('}')
    top = savedEnv
    return s

def decls():
    global used
    while look.tag == Lexer.Tag.BASIC:
        p = type()
        tok = look
        match(Lexer.Tag.ID)
        match(';')
        id = Id(Word(tok), p, used)
        top[tok] = id
        used += p.width

def type():
    p = look
    match(Lexer.Tag.BASIC)
    if look.tag != '[':
        return p
    else:
        return dims(p)

def dims(p):
    match('[')
    tok = look
    match(lexer.Tag.NUM)
    match(']')
    if look.tag == '[':
        p = dims(p)
    return Array(tok.value, p)

def stmts():
    if look.tag == '}':
        return Stmt.Null
    else:
        return Seq(stmt(), stmts())

def stmt():
    x = None
    s = None
    sl = None
    s2 = None
    savedStmt = None

    if look.tag == ';':
        move()
        return Stmt.Null
    elif look.tag == Tag.IF:
        move()
        match('(')
        x = bool()
        match(')')
        sl = stmt()

        if look.tag != Tag.ELSE:
            return If(x, sl)
        else:
            match(Tag.ELSE)
            s2 = stmt()
            return Else(x, sl, s2)
    elif look.tag == Tag.WHILE:
        whilenode = While()
        savedStmt = Stmt.Enclosing
        Stmt.Enclosing = whilenode
        move()
        match('(')
        x = bool()
        match(')')
        sl = stmt()
        whilenode.init(x, sl)
        Stmt.Enclosing = savedStmt
        return whilenode
    elif look.tag == Tag.DO:
        donode = Do()
        savedStmt = Stmt.Enclosing
        Stmt.Enclosing = donode
        move()
        sl = stmt()
        match(Tag.WHILE)
        match('(')
        x = bool()
        match(')')
        match(';')
        donode.init(sl, x)
        Stmt.Enclosing = savedStmt
        return donode
    elif look.tag == Tag.BREAK:
        match(Tag.BREAK)
        match(';')
        return Break()
    elif look.tag == '{':
        return block()
    else:
        return assign()

def assign():
    global stmt
    t = look
    match(Tag.ID)
    id = top.get(t)
    if id is None:
        error(f"{t} undeclared")

    if look.tag == '=':
        move()
        stmt = Set(id, bool())
    else:
        x = offset(id)
        match('=')
        stmt = SetElem(x, bool())
        match(';')

    return stmt

def bool():
    x = join()
    while look.tag == Tag.OR:
        tok = look
        move()
        x = Or(tok, x, join())
    return x

def join():
    x = equality()
    while look.tag == Tag.AND:
        tok = look
        move()
        x = And(tok, x, equality())
    return x

def equality():
    x = rel()
    while look.tag == Tag.EQ or look.tag == Tag.NE:
        tok = look
        move()
        x = Rel(tok, x, rel())
    return x

def rel():
    x = expr()
    if look.tag in ['<', Tag.LE, Tag.GE, '>']:
        tok = look
        move()
        return Rel(tok, x, expr())
    return x

def expr():
    x = term()
    while look.tag == '+' or look.tag == '-':
        tok = look
        move()
        x = Arith(tok, x, term())
    return x

def term():
    x = unary()
    while look.tag == '*' or look.tag == '/':
        tok = look
        move()
        x = Arith(tok, x, unary())
    return x

def unary():
    if look.tag == '-':
        move()
        return Unary(Word('minus'), unary())
    elif look.tag == '!':
        tok = look
        move()
        return Not(tok, unary())
    else:
        return factor()

def factor():
    global x
    if look.tag == '(':
        move()
        x = bool()
        match(')')
        return x
    elif look.tag == Tag.NUM:
        x = Constant(look, Type.Int)
        move()
        return x
    elif look.tag == Tag.REAL:
        x = Constant(look, Type.Float)
        move()
        return x
    elif look.tag == Tag.TRUE:
        x = Constant(True)
        move()
        return x
    elif look.tag == Tag.FALSE:
        x = Constant(False)
        move()
        return x
    elif look.tag == Tag.ID:
        s = str(look)
        id = top.get(look)
        move()

        if look.tag != '[':
            return id
        else:
            return offset(id)

def offset(a):
    global x
    match('[')
    i = bool()
    match(']')
    type = a.type
    type = type.of
    w = Constant(type.width)
    tl = Arith(Token('*'), i, w)
    loc = tl

    while look.tag == '[':
        match('[')
        i = bool()
        match(']')
        type = type.of
        w = Constant(type.width)
        tl = Arith(Token('*'), i, w)
        t2 = Arith(Token('+'), loc, tl)
        loc = t2

    return Access(a, loc, type)


lex = None  # Your lexer implementation goes here
look = None

# You may need to define the necessary classes like Id, Stmt, Expr, etc. based on your code's context.

# Now you can call the `program()` function to start parsing.

