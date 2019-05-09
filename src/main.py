import sys

from PyMIPS.lexer import lex
from PyMIPS.AST.ast import parse
from PyMIPS.Datastructure.execution_stack import run_program

if __name__ == "__main__":

    filename = sys.argv[1]
    with open(filename) as file:
        characters = file.read()
    tokens = lex(characters)
    try:
        res = parse(tokens)
    except Exception as e:
        print(e)
        sys.exit(1)
    run_program(res.value)

