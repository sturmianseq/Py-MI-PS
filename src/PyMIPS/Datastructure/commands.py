import sys

from PyMIPS.Datastructure.register import RegisterPool
from PyMIPS.Datastructure.immediate import StoredRefs
from PyMIPS.Datastructure.data_model import data_stack


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
        command.destination_register.set_contents(command.immediate)

    return exe


def lw_command(command):
    def exe():
        command.destination_register.set_contents(command.immediate)

    return exe


def add_command(command):
    def exe():
        dest = command.destination_register
        res = (
            command.source_register.get_contents()
            + command.target_register.get_contents()
        )
        dest.set_contents(lambda: res)

    return exe


def sub_command(command):
    def exe():
        dest = command.destination_register
        res = (
            command.source_register.get_contents()
            - command.target_register.get_contents()
        )
        dest.set_contents(lambda: res)

    return exe


def sw_command(command):
    def store_into_label():
        contents = command.destination_register.get_contents()
        StoredRefs.store_ref(command.immediate._value, lambda: contents)

    def store_on_stack():
        value = command.destination_register.get_contents()
        offset = command.immediate()
        register = command.source_register.name
        data_stack.store_word(offset, value, register=register)

    if command.source_register:
        return store_on_stack
    else:
        return store_into_label


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

