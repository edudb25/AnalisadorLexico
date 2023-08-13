# Variáveis globais simulando a propriedade de classes
lexline = 0
labels = 0

def error(s):
    raise Exception("near line " + str(lexline) + ": " + s)

def newlabel():
    global labels
    labels = labels + 1
    return labels

def emitlabel(i):
    print("L" + str(i) + ":")

def emit(s):
    print("\t" + s)

