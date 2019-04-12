from PyMIPS.lexer import *


def parse(tokens):
    return tokens_to_context(tokens)


def tokens_to_context(tokens):
    return Context(".text") | Context("data")


def tokens_to_lines(tokens):
    result = []
    current = []
    for t in tokens:
        value, tag = t
        if tag is NEWLINE:
            if len(current) != 0:
                result.append(current)
            current = []
            continue
        current.append(t)
    return result


class Parser:
    def __call__(self, tokens, pos):
        return None

    def __or__(self, other):
        return Alternator(self, other)


class Alternator(Parser):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __call__(self, tokens, pos):
        first_result = self.first()
        if not first_result:
            return self.second()
        return first_result
