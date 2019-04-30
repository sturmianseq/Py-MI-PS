class StoredRefs:
    __storage = {}

    @staticmethod
    def store_ref(key, value):
        StoredRefs.__storage[key] = value

    @staticmethod
    def get_ref(key):
        return StoredRefs.__storage[key]

    @staticmethod
    def print_all_active_refs():
        for key in StoredRefs.__storage:
            print(f"{key}: {StoredRefs.__storage[key]()}")


class Immediate:
    def __init__(self, value):
        self._value = value

    def __call__(self):
        return self._value()

    def __repr__(self):
        return f"Immediate({self()})"


class Ref_Immediate(Immediate):
    def __call__(self):
        return StoredRefs.get_ref(self._value)()
