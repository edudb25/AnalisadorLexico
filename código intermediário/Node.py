class Node:
    def __init__(self):
        self.lexline = 0
        self.lexline = Lexer.line

    def error(self, s):
        raise Error("near line" + str(self.lexline) + ": " + s)

    labels = 0

    def newlabel(self):
        labels = labels + 1
        return labels

    def emitlabel(self, i):
        print("L" + str(i) + ":")

    def emit(self, s):
        print("\t" + s)
