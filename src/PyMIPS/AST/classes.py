from PyMIPS.lexer import *
from PyMIPS.Datastructure.commands import get_command
from PyMIPS.AST.validator import validate


class I_Type:
    def __init__(self, contents):
        self.command = None
        self.target_register = None
        self.source_register = None
        self.immediate = None
        up = epic_unpack(contents)
        # if not validate(self):
        # raise Exception("Illegal arguments")
        {4: self.set_4, 6: self.set_6}[len(up)](up)
        # self.func = get_command(self)

    def set_4(self, contents):
        self.command = contents[2]
        self.target_register = contents[3]
        self.immediate = contents[0]

    def set_6(self, contents):
        self.command = contents[2]
        self.target_register = contents[4]
        self.source_register = contents[3]
        self.immediate = contents[0]

    def __repr__(self):
        return f"I_Type({self.command} {self.target_register}, {self.source_register}, {self.immediate})"


class R_Type:
    def __init__(self, contents):
        self.command = None
        self.destination = None
        self.r1 = None
        self.r2 = None
        self.shift_amount = None
        up = special_unpack(contents)
        # if not validate(self):
        # raise Exception("Illegal arguments")
        {1: self.set_1, 4: self.set_4, 6: self.set_6}[len(up)](up)
        # self.func = get_command(self)

    def set_1(self, contents):
        self.command = contents[0]

    def set_4(self, contents):
        self.command = contents[0]
        self.destination = contents[1]
        self.r1 = contents[3]

    def set_6(self, contents):
        self.command = contents[0]
        self.destination = contents[1]
        self.r1 = contents[3]
        self.r2 = contents[5]

    def __repr__(self):
        return f"R_Type({self.command} {self.destination}, {self.r1}, {self.r2})"


class J_Type:
    def __init__(self, command, address):
        self.command = command
        self.address = address
        # if not validate(self):
        # raise Exception("Illegal arguments")

    def __repr__(self):
        return f"{self.command}({self.address})"


def rev_unpack(contents: tuple) -> list:
    result = []
    while type(contents) == tuple:
        contents, value = contents
        result.append(value)
    result.append(contents)
    result.reverse()
    return result


def special_unpack(contents: tuple) -> list:
    if type(contents) != tuple:
        return [contents]
    result = []
    command, contents = contents
    while type(contents) == tuple:
        contents, value = contents
        result.append(value)
    result.append(contents)
    result.append(command)
    result.reverse()
    return result


def epic_unpack(contents) -> list:
    # Check to see if tuple
    if type(contents) != tuple:
        return [contents]
    result = []
    while type(contents) == tuple:
        value, contents = contents
        if type(value) == tuple:
            value, contents = contents, value

        result.append(value)
    result.append(contents)
    return result

