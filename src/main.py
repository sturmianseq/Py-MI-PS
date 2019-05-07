import sys

from PyMIPS.tests.example1_test import test_example1

if __name__ == "__main__":
    """
    filename = sys.argv[1]
    with open(filename) as file:
        characters = file.read()
    tokens = lex(characters)
    #print(tokens)
    #print("\n\n")
    res = parse(tokens)
    print(res)
    """
    test_example1()

