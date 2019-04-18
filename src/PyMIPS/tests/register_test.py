from PyMIPS.Datastructure.register import *


def test_setting_to_num():
    rp = RegisterPool.get_instance()
    t1 = rp.get_register("$t1")
    assert t1.get_contents() == 0
    t1.set_contents(12)
    assert t1.get_contents() == 12
