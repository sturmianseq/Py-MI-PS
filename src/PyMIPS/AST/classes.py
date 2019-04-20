from PyMIPS.lexer import *


class I_Type:
    def __init__(self, command, target_register, source_register=None, immediate=None):
        self.command = command
        self.target_register = target_register
        self.source_register = source_register
        self.immediate = immediate

    def __repr__(self):
        return f"I_Type({self.command} {self.target_register}, {self.source_register}, {self.immediate})"


class R_Type:
    def __init__(self, command, destination, r1=None, r2=None, shift_amount=0):
        self.command = command
        self.destination = destination
        self.r1 = r1
        self.r2 = r2
        self.shift_amount = shift_amount

    def __repr__(self):
        return f"R_Type({self.command} {self.destination}, {self.r1}, {self.r2})"


class J_Type:
    def __init__(self, command, address):
        self.command = command
        self.address = address

    def __repr__(self):
        return f"{self.command}({self.address})"

