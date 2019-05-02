"""Data Stack Module

This module houses the DataStack class which is used to replecate MIPS memory access
"""

from PyMIPS.AST.class_utils import create_register


class DataStack:
    def __init__(self, allocated_space=1024):
        """The DataStack replicates MIPS memory access
        
        Parameters
        ----------
        allocated_space : int, optional
            The amount of allocated space, by default 1024
        """
        self.allocated_space = 1024
        self.sp = create_register("$sp")
        self.sp.set_contents(lambda: allocated_space)
        self.stack = {}

    def store_word(self, offset: int, value: callable, register="$sp"):
        """Replicates the store word functionality of MIPS
        
        Parameters
        ----------
        offset : int
            Offset from the register
        value : callable
            The contained value as a callable
        register : str, optional
            The register to offset from, by default "$sp"
        
        Raises
        ------
        Exception
            If the offset isn't divisible by 4, a Bad Access error rises
        """
        # For now, make sure the offset is divisible by 4
        if offset % 4 != 0:
            raise Exception("Bad access")

        # Get the offset register
        r = create_register(register)

        # Calculate the location
        location = r.get_contents() + offset

        # Set it
        self.stack[location] = value

    def load_word(self, offset: int, register="$sp") -> callable:
        """Replicates the load word functionality of mips
        
        Parameters
        ----------
        offset : int
            Offset from register
        register : str, optional
            The register to offset, by default "$sp"
        
        Returns
        -------
        callable
            The value stored in the load word as a callable
        
        Raises
        ------
        Exception
            If the offset isn't divisible by 4, a Bad Access error rises
        """

        # For now, make sure the offset is divisible by 4
        if offset % 4 != 0:
            raise Exception("Bad access")

        # Get the offset register
        r = create_register(register)

        # Calculate the location
        location = r.get_contents() + offset

        return self.stack[location]

    def print_stack(self):
        for key in self.stack:
            print(f"Address({key}): {self.stack[key]}")


# Exports
data_stack = DataStack()
