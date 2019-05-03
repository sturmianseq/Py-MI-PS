from PyMIPS.Datastructure.commands import get_command
from PyMIPS.AST.class_utils import create_register, create_immediate


class Command:
    def __init__(self):
        """Base Command Class
        """
        self.command = None
        self.destination_register = None  # The register to be mutated
        self.source_register = None  # The source register
        self.target_register = None  # The second source register
        self.shamt = None  # Shift amount
        self.immediate = None  # Immediate
        self.address = None  # Address for J Types
        self.func = lambda: False

    def __call__(self):
        return self.func()


class I_Type(Command):
    def __init__(self, command: str, destination: str, immediate, source: str = None):
        """Stores I_Type commands
        
        Parameters
        ----------
        command : str
            An I_Type command string
        destination : str
            Name of destination register
        immediate : any
            An immediate (See immediate for details)
        source : str, optional
            Name of source register, by default None
        """
        super().__init__()
        self.command = command
        self.destination_register = create_register(destination)
        self.source_register = create_register(source)
        self.immediate = create_immediate(immediate)
        self.func = get_command(self)

    def __repr__(self):
        return f"I_Type({self.command} {self.destination_register}, {self.source_register}, {self.immediate})"


class R_Type(Command):
    def __init__(
        self,
        command: str,
        destination: str,
        source_register: str = None,
        target_register: str = None,
        shamt: int = 0,
    ):
        """Stores R_Type commands
        
        Parameters
        ----------
        command : str
            R Type command string
        destination : str
            Destination register name
        source_register : str, optional
            Source register name, by default None
        target_register : str, optional
            Target register name, by default None
        shamt : int, optional
            Shift amount, by default 0
        """
        super().__init__()
        self.command = command
        self.destination_register = create_register(destination)
        self.source_register = create_register(source_register)
        self.target_register = create_register(target_register)
        self.shamt = shamt
        self.func = get_command(self)

    def __repr__(self):
        return f"R_Type({self.command} {self.destination_register}, {self.source_register}, {self.target_register})"


class J_Type(Command):
    def __init__(self, command: str, address):
        """Stores J Type commands
        
        Parameters
        ----------
        command : str
            J type command string
        address : not sure yet
            TODO
        """
        super().__init__()
        self.command = command
        self.address = address

    def __repr__(self):
        return f"{self.command}({self.address})"


def unpack(contents) -> list:
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

