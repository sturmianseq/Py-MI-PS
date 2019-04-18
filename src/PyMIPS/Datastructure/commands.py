import sys

from PyMIPS.AST.classes import I_Type, R_Type, J_Type
from PyMIPS.Datastructure.register import RegisterPool
from PyMIPS.Datastructure.immediate import StoredRefs


def li_command(command: I_Type):
    def exe():
        command.target_register.set_contents(command.immediate)

    return exe


def lw_command(command: I_Type):
    def exe():
        command.target_register.set_contents(command.immediate)

    return exe


def add_command(command: R_Type):
    def exe():
        dest = command.destination
        res = command.r1.get_contents() + command.r2.get_contents()
        dest.set_contents(lambda: res)

    return exe


def sub_command(command: R_Type):
    def exe():
        dest = command.destination
        res = command.r1.get_contents() - command.r2.get_contents()
        dest.set_contents(lambda: res)

    return exe


def sw_command(command: I_Type):
    def exe():
        contents = command.target_register.get_contents()
        StoredRefs.store_ref(command.immediate._value, contents)

    return exe


def syscall_command(command: R_Type):
    rp = RegisterPool.get_instance()
    v0 = rp.get_register("$v0")

    def print_int():
        pass

    def print_float():
        pass

    def print_double():
        pass

    def print_string():
        pass

    def read_int():
        pass

    return {
        1: print_int,
        2: print_float,
        3: print_double,
        4: print_string,
        5: read_int,
        10: sys.exit,
    }[v0.get_contents()]

