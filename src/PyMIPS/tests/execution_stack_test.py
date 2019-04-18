from PyMIPS.Datastructure.commands import *


def test_li():
    c = I_Type("li", target_register="$t0", immediate=6)
    rp = RegisterPool.get_instance()
    t0 = rp.get_register("$t0")
    assert t0.get_contents() == 0
    f = li_command(c)
    assert t0.get_contents() == 0
    f()
    assert t0.get_contents() == 6
