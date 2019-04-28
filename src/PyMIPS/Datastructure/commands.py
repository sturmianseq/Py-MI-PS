import sys

from PyMIPS.Datastructure.register import RegisterPool
from PyMIPS.Datastructure.immediate import StoredRefs


def get_command(ast_class):
    return {
        "li": li_command,
        "lw": lw_command,
        "sw": sw_command,
        "add": add_command,
        "sub": sub_command,
        "syscall": syscall_command,
    }[ast_class.command](ast_class)


def li_command(command):
    def exe():
        command.target_register.set_contents(command.immediate)

    return exe


def lw_command(command):
    def exe():
        command.target_register.set_contents(command.immediate)

    return exe


def add_command(command):
    def exe():
        dest = command.destination
        res = command.r1.get_contents() + command.r2.get_contents()
        dest.set_contents(lambda: res)

    return exe


def sub_command(command):
    def exe():
        dest = command.destination
        res = command.r1.get_contents() - command.r2.get_contents()
        dest.set_contents(lambda: res)

    return exe


def sw_command(command):
    def exe():
        contents = command.target_register.get_contents()
        StoredRefs.store_ref(command.immediate._value, contents)

    return exe


def syscall_command(command):
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

    def exe():
        return {
            1: print_int,
            2: print_float,
            3: print_double,
            4: print_string,
            5: read_int,
            10: sys.exit,
        }[v0.get_contents()]

    return exe

