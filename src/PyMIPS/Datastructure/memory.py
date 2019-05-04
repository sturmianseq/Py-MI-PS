class MemoryBlock:
    def __init__(self, value, base_address: int, size: int):
        """Handles maintaining memory blocks
        
        Parameters
        ----------
        value : Any
            The value stored in the block
        base_address : int
            The beginning address of the data
        size : int
            The size of the data block
        """
        self.value = value
        self.base_address = base_address
        self.size = size

    def __call__(self, address: int):
        """Returns the stored data given an address
        
        Parameters
        ----------
        address : int
            The address to access
        
        Returns
        -------
        Any
            The stored value
        
        Raises
        ------
        Exception
            Bad Access
        Exception
            Memory Corrupted
        """
        if address != self.base_address:
            raise Exception(f"Bad Access: {address}")
        data = Memory.get_data()
        for i in range(1, self.size):
            new_val = data[address + i]
            if new_val.base_address != self.base_address:
                raise Exception(f"Memory Corrupted: {address}")

        return self.value


class Memory:
    __data = {}

    @staticmethod
    def store_value(value, address: int, size=4):
        """Store a value in static memory
        
        Parameters
        ----------
        value : Any
            A value to store in memory
        address : int
            The address to store the value
        size : int, optional
            The size in bytes of the value, by default 4
        """
        for i in range(size):
            Memory.__data[address + i] = MemoryBlock(value, address, size)

    @staticmethod
    def get_value(address: int):
        """Retrives a value from memory
        
        Parameters
        ----------
        address : int
            The address to access
        
        Returns
        -------
        Any
            The value stored
        """
        if address not in Memory.__data.keys():
            return 0

        return Memory.__data[address](address)

    @staticmethod
    def get_data():
        return Memory.__data
