from PyMIPS.lexer import *
from PyMIPS.parser import *


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


class Move:
    def __init__(self, dest, src):
        self.dest = dest
        self.src = src

    def __repr__(self):
        return f"MOVE {self.dest} <- {self.src}"


class Syscall:
    def __repr__(self):
        return "SYSCALL"


# Defs
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


def move_type():
    def process(parsed):
        (((_, d), _), s) = parsed
        return Move(d, s)

    return (
        Reserved("move", COMMAND) + Tag(REGISTER) + Tag(SEPERATOR) + Tag(REGISTER)
        ^ process
    )


def syscall():
    def process(parsed):
        return Syscall()

    return Reserved("syscall", COMMAND) ^ process


def command_list():
    return i_type() | i_type_with_ref() | r_type() | syscall() | move_type()
