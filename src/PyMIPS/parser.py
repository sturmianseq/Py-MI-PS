from PyMIPS.lexer import *


def prepare(tokens):
    return tokens_to_context(tokens)


def tokens_to_context(tokens):
    lines = tokens_to_lines(tokens)
    result = []
    for line in lines:
        result += line
        # result += [("NEWLINE", NEWLINE)]
    return result


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


class Result:
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos

    def __repr__(self):
        return f"Result({self.value}, {self.pos})"


class Parser:
    def __call__(self, tokens, pos):
        return None

    def __add__(self, other):
        return Concat(self, other)

    def __xor__(self, function):
        return Process(self, function)

    def __mul__(self, other):
        return Exp(self, other)

    def __or__(self, other):
        return Alternator(self, other)


class Alternator(Parser):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __call__(self, tokens, pos):
        first_result = self.first(tokens, pos)
        if not first_result:
            return self.second(tokens, pos)
        return first_result


class Tag(Parser):
    def __init__(self, name):
        self.name = name

    def __call__(self, tokens, pos):
        if pos < len(tokens) and tokens[pos][1] is self.name:
            return Result(tokens[pos][0], pos + 1)
        return None


class Reserved(Parser):
    def __init__(self, name, tag):
        self.name = name
        self.tag = tag

    def __call__(self, tokens, pos):
        if (
            pos < len(tokens)
            and tokens[pos][0] == self.name
            and tokens[pos][1] is self.tag
        ):
            return Result(tokens[pos][0], pos + 1)


class Concat(Parser):
    def __init__(self, left: Parser, right: Parser):
        self.left = left
        self.right = right

    def __call__(self, tokens, pos):
        left_res = self.left(tokens, pos)
        if left_res:
            right_res = self.right(tokens, left_res.pos)
            if right_res:
                combined = (left_res.value, right_res.value)
                return Result(combined, right_res.pos)
        return None


class Lazy(Parser):
    def __init__(self, parser_func):
        self.parser = None
        self.parser_func = parser_func

    def __call__(self, tokens, pos):
        if not self.parser:
            self.parser = self.parser_func()
        return self.parser(tokens, pos)


class Process(Parser):
    def __init__(self, parser, function):
        self.parser = parser
        self.function = function

    def __call__(self, tokens, pos):
        result = self.parser(tokens, pos)
        if result:
            result.value = self.function(result.value)
            return result


class Exp(Parser):
    def __init__(self, parser, separator):
        self.parser = parser
        self.separator = separator

    def __call__(self, tokens, pos):
        result = self.parser(tokens, pos)

        def process_next(parsed):
            (sepfunc, right) = parsed
            return sepfunc(result.value, right)

        next_parser = self.separator + self.parser ^ process_next

        next_result = result
        while next_result:
            next_result = next_parser(tokens, result.pos)
            if next_result:
                result = next_result
        return result

