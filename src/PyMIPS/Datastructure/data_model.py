"""Data Stack Module

This module houses the DataStack class which is used to replecate MIPS memory access
"""
try:
    from src.PyMIPS.AST.class_utils import create_register
    from src.PyMIPS.Datastructure.memory import Memory
except:
    from PyMIPS.AST.class_utils import create_register
    from PyMIPS.Datastructure.memory import Memory


class DataStack:
    __stack_pointer = create_register("$sp")
    __stack_size = 0

    @staticmethod
    def alloc(stack_size: int):
        _DataStack__stack_size = Memory.alloc(stack_size)
        DataStack.__stack_pointer.set_contents(lambda: _DataStack__stack_size)

    @staticmethod
    def store_word(offset: int, value: callable, register="$sp"):
        """Replicates the store word functionality of MIPS
        
        Parameters
        ----------
        offset : int
            Offset from the register
        value : callable
            The contained value as a callable
        register : str, optional
            The register to offset from, by default "$sp"
        """
        # Get the offset register
        r = create_register(register)

        # Calculate the location
        location = r.get_contents() + offset

        # Set it
        Memory.store_value(value, location)

    @staticmethod
    def load_word(offset: int, register="$sp") -> callable:
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
        """
        # Get the offset register
        r = create_register(register)

        # Calculate the location
        location = r.get_contents() + offset

        return Memory.get_value(location)


class DataHeap:
    __next_address = 0
    __refs = {}

    @staticmethod
    def alloc(heap_size: int):
        _DataHeap__next_address = Memory.alloc(heap_size)

    @staticmethod
    def store(value, label, size=4):
        DataHeap.__next_address -= size
        Memory.store_value(value, DataHeap.__next_address, size)
        DataHeap.__refs[label] = DataHeap.__next_address

    @staticmethod
    def get_address(label):
        if label in DataHeap.__refs.keys():
            return DataHeap.__refs[label]
        raise Exception(f"Heap Address Not Found: {label}")

    @staticmethod
    def get_value(label):
        address = DataHeap.get_address(label)
        return Memory.get_value(address)

