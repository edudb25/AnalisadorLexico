lexline = 0
labels = 0

def Node():
    global lexline
    lexline = Lexer.line

def error(s):
    raise Error("near line" + str(lexline) + ": " + s)

def newlabel():
    global labels
    labels += 1
    return labels

def emitlabel(i):
    print("L" + str(i) + ":")

def emit(s):
    print("\t" + s)
