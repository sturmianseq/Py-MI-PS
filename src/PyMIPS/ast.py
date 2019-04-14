from PyMIPS.parser import *
from PyMIPS.lexer import *


class Globl:
    def __init__(self, entry):
        self.entry = entry

    def __repr__(self):
        return f"Entry Point: {self.entry}"


class TextBlock:
    def __init__(self, contents):
        self.contents = contents

    def __repr__(self):
        c = str(self.contents)
        return f"Text Block: {c}"


class DataBlock:
    def __init__(self, contents):
        self.contents = contents

    def __repr__(self):
        c = str(self.contents)
        return f"Data Block: {c}"


class I_Type:
    def __init__(self, command, register, immediate):
        self.command = command
        self.register = register
        self.immediate = immediate

    def __repr__(self):
        return f"I_Type({self.command} {self.register}, {self.immediate})"


class R_Type:
    def __init__(self, command, destination, r1, r2):
        self.command = command
        self.destination = destination
        self.r1 = r1
        self.r2 = r2

    def __repr__(self):
        return f"R_Type({self.command} {self.destination}, {self.r1}, {self.r2})"


class Label:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

    def __repr__(self):
        return f"{self.name} {str(self.contents)}"


class Syscall:
    def __repr__(self):
        return "SYSCALL"


class WordDeclaration:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"{self.name} {self.size}"


class Asciiz:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

    def __repr__(self):
        return f"{self.name} {self.contents}"


def parser():
    return blocks() + Lazy(parser) | blocks()


def blocks():
    return globl_block() | text_block() | data_block()


def data_block():
    def process(parsed):
        _, value = parsed
        return DataBlock(value)

    return (Reserved(".data", DIRECTIVE) + data_contents()) ^ process


def data_contents():
    return data_declaration() + Lazy(data_contents) | data_declaration()


def data_declaration():
    return word_declaration() | asciiz_declaration()


def word_declaration():
    def process(parsed):
        ((name, _), size) = parsed
        return WordDeclaration(name, size)

    return Tag(LABEL) + Tag(DIRECTIVE) + Tag(INT) ^ process


def asciiz_declaration():
    def process(parsed):
        ((name, _), size) = parsed
        return Asciiz(name, size)

    return Tag(LABEL) + Tag(DIRECTIVE) + Tag(STRING) ^ process


def globl_block():
    def process(parsed):
        _, v = parsed
        return Globl(v)

    return Reserved(".globl", DIRECTIVE) + Tag(REFERENCE) ^ process


def text_block():
    def process(parsed):
        _, value = parsed
        return TextBlock(value)

    return (Reserved(".text", DIRECTIVE) + contents()) ^ process


def contents():
    return (label_group() | globl_block()) + Lazy(contents) | (
        label_group() | globl_block()
    )


def label_group():
    def process(parsed):
        name, contents = parsed
        return Label(name, contents)

    return Tag(LABEL) + command() ^ process


def command():
    return command_list() + Lazy(command) | command_list()


def command_list():
    return i_type() | i_type_with_ref() | r_type() | syscall()


def syscall():
    def process(parsed):
        return Syscall()

    return Reserved("syscall", COMMAND) ^ process


def i_type():
    def process(parsed):
        (((c, r), _), i) = parsed
        return I_Type(c, r, i)

    return Tag(COMMAND) + Tag(REGISTER) + Tag(SEPERATOR) + Tag(INT) ^ process


def i_type_with_ref():
    def process(parsed):
        (((c, r), _), i) = parsed
        return I_Type(c, r, i)

    return Tag(COMMAND) + Tag(REGISTER) + Tag(SEPERATOR) + Tag(REFERENCE) ^ process


def r_type():
    def process(parsed):
        (((((c, rd), _), r1), _), r2) = parsed
        return R_Type(c, rd, r1, r2)

    return (
        Tag(COMMAND)
        + Tag(REGISTER)
        + Tag(SEPERATOR)
        + Tag(REGISTER)
        + Tag(SEPERATOR)
        + Tag(REGISTER)
        ^ process
    )
