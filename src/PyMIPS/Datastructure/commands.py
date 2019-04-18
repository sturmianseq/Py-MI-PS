from PyMIPS.AST.commands import I_Type
from PyMIPS.Datastructure.register import RegisterPool


def li_command(command: I_Type):
    def exe():
        rp = RegisterPool.get_instance()
        dest = rp.get_register(command.target_register)
        dest.set_contents(command.immediate)

    return exe
