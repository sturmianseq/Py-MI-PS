from PyMIPS.AST.blocks import *
from PyMIPS.AST.classes import *
from PyMIPS.AST.data import *


def parser():
    def process(parsed):
        return Program(parsed)

    return program() ^ process


def program():

    return blocks() + Lazy(program) | blocks()


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
