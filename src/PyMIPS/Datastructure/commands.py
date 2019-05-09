import sys

from PyMIPS.Datastructure.data_model import RegisterPool, DataHeap, DataStack


def get_command(ast_class):
    return {
        "li": li_command,
        "lw": lw_command,
        "sw": sw_command,
        "add": add_command,
        "sub": sub_command,
        "syscall": syscall_command,
        "mflo": mflo_command,
        "mfhi": mfhi_command,
        "div": div_command,
        "move": move_command,
        "addi": addi_command,
    }[ast_class.command](ast_class)


def move_command(command):
    def exe():
        source = command.source_register.get_contents()
        command.destination_register.set_contents(source)

    return exe


def li_command(command):
    def exe():
        command.destination_register.set_contents(command.immediate)

    return exe


def lw_command(command):
    def exe():
        command.destination_register.set_contents(command.immediate)

    return exe


def mflo_command(command):
    def exe():
        mflo = RegisterPool.get_register("$mflo")
        command.destination_register.set_contents(mflo.get_contents())

    return exe


def mfhi_command(command):
    def exe():
        mfhi = RegisterPool.get_register("$mfhi")
        command.destination_register.set_contents(mfhi.get_contents())

    return exe


def div_command(command):
    def exe():
        quotient_res = (
            command.source_register.get_contents()
            // command.destination_register.get_contents()
        )
        remainder_res = (
            command.source_register.get_contents()
            % command.destination_register.get_contents()
        )
        mfhi = RegisterPool.get_register("$mfhi")
        mflo = RegisterPool.get_register("$mflo")
        mfhi.set_contents(lambda: remainder_res)
        mflo.set_contents(lambda: quotient_res)

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
        DataHeap.store(contents, command.immediate._value)

    def store_on_stack():
        value = command.destination_register.get_contents()
        offset = command.immediate()
        register = command.source_register.name
        DataStack.store_word(offset, value, register=register)

    if command.source_register:
        return store_on_stack
    else:
        return store_into_label


def addi_command(command):
    """
    addi $dest, $targ, immediate
    """

    def exe():
        dest = command.destination_register
        res = command.target_register.get_contents() + command.immediate()
        dest.set_contents(lambda: res)

    return exe


def syscall_command(command):
    rp = RegisterPool
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

