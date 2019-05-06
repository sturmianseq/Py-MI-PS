try:
    from src.PyMIPS.Datastructure.memory import Memory
except:
    from PyMIPS.Datastructure.memory import Memory

import unittest


class TestMemory(unittest.TestCase):
    def test_storage(self):
        Memory.store_value(16, 2214)
        Memory.store_value(17, 2014)

        self.assertEqual(Memory.get_value(2214), 16)
        self.assertEqual(Memory.get_value(2014), 17)

    def test_bad_access(self):
        Memory.store_value(16, 2000)

        with self.assertRaises(Exception):
            Memory.get_value(2001)
            Memory.get_value(2002)
            Memory.get_value(2003)
        try:
            Memory.get_value(2004)
        except:
            self.fail("Memory 2004 should be avalible")

    def test_overwrite(self):
        Memory.store_value(16, 2000)
        self.assertEqual(Memory.get_value(2000), 16)

        Memory.store_value(20, 2001)
        self.assertEqual(Memory.get_value(2001), 20)

        with self.assertRaises(Exception):
            Memory.get_value(2000)
