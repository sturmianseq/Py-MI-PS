from PyMIPS.AST.combinators import *
from PyMIPS.AST.classes import *
from PyMIPS.AST.blocks import *
from PyMIPS.lexer import *


def global_directive():
    def exe(data):
        (_, ref) = data
        return Globl(ref)

    return Tag(DIRECTIVE) + Tag(REFERENCE) ^ exe


def text_parser():
    return text_statements() + Lazy(text_parser) | text_statements()


def text_statements():
    return label_block() | global_directive()


def label_block():
    def process(data):
        name, contents = data
        return Label(name, contents)

    return Tag(LABEL) + command_iterator() ^ process


def command_iterator():
    return command_list() + Lazy(command_iterator) | command_list()


def command_list():
    return i_type() | r_type() | syscall() | j_type()


def i_type():
    def process(data):
        return I_Type(data)

    return (
        Tag(COMMAND)
        + ((Tag(REGISTER) + Tag(SEPERATOR) + Tag(REGISTER)) | (Tag(REGISTER)))
        + Tag(SEPERATOR)
        + (Tag(INT) | Tag(REFERENCE))
    ) ^ process


def i_type_with_offset():
    return None


def r_type():
    def process(data):
        return R_Type(data)

    return (
        Tag(COMMAND)
        + (
            (
                Tag(REGISTER)
                + Tag(SEPERATOR)
                + Tag(REGISTER)
                + Tag(SEPERATOR)
                + Tag(REGISTER)
            )
            | (Tag(REGISTER) + Tag(SEPERATOR) + Tag(REGISTER))
            | Tag(REGISTER)
        )
        ^ process
    )


def syscall():
    def process(data):
        return R_Type("syscall")

    return Keyword("syscall", COMMAND) ^ process


def j_type():
    def process(data):
        command, ref = data
        return J_Type(command, ref)

    return (Keyword("j", COMMAND) | Keyword("jal", COMMAND)) + Tag(REFERENCE) ^ process
