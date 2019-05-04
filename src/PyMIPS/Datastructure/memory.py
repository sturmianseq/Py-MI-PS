class MemoryBlock:
    def __init__(self, value, base_address, size):
        self.value = value
        self.base_address = base_address
        self.size = size

    def __call__(self, address):
        if address != self.base_address:
            raise Exception(f"Bad Access: {address}")

        for i in range(1, self.size):
            new_val = Memory.__data[address + i]
            if new_val

class Memory:
    __data = {}

    @staticmethod
    def store_value(value, address: int, size=4):
        for i in range(size):
            Memory.__data[address + i]

    @staticmethod
    def get_value(address: int):
        if address not in Memory.__data.keys():
            return 0

        value = Memory.__data[address]
        if value.base_address == address:
            return value.value
        else:
            raise Exception(f"Bad Access: {address}")
