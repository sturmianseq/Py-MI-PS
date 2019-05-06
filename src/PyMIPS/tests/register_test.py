from PyMIPS.Datastructure.data_model import RegisterPool as rp


def test_setting_to_num():
    t1 = rp.get_register("$t1")
    assert t1.get_contents() == 0
    t1.set_contents(lambda: 12)
    assert t1.get_contents() == 12
