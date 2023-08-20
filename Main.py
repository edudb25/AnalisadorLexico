import sys
from Lexer import Lexer
from Parser import Parser

def main():
    try:
        lex = Lexer()
        parse = Parser(lex)
        parse.program()
        sys.stdout.write('\n')
    except Exception as e:
        sys.stderr.write(f'Error: {str(e)}\n')

if __name__ == "__main__":
    main()
