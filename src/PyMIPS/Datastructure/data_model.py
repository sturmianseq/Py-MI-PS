"""Data Stack Module

This module houses the DataStack class which is used to replecate MIPS memory access
"""

from PyMIPS.Datastructure.memory import Memory


class Immediate:
    def __init__(self, value):
        self._value = value

    def __call__(self):
        return self._value()

    def __repr__(self):
        return f"Immediate({self()})"


class RefImmediate(Immediate):
    def __call__(self):
        return DataHeap.get_value(self._value)


class Register:
    def __init__(self, name):
        self.name = name
        self.__contents = lambda: 0

    def __repr__(self):
        return f"Register({self.name}, {str(self.__contents())})"

    def set_contents(self, value):
        self.__contents = value

    def get_contents(self):
        return self.__contents()


class RegisterPool:
    """RegisterPool is a collection of static methods that handle register interactions
    """

    __registers = {"$zero": Register("$zero")}

    @staticmethod
    def print_all_active_registers():
        for key in RegisterPool.__registers:
            print(RegisterPool.__registers[key])

    @staticmethod
    def get_register(name: str) -> Register:
        if name in RegisterPool.__registers.keys():
            return RegisterPool.__registers[name]
        else:
            reg = Register(name)
            RegisterPool.__registers[name] = reg
            return reg


def create_immediate(value) -> Immediate:
    if type(value) == int:
        return Immediate(lambda: value)
    if type(value) == str:
        return RefImmediate(value)
    return None


def create_register(value) -> Register:
    if value is None:
        return None
    return RegisterPool.get_register(value)


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
