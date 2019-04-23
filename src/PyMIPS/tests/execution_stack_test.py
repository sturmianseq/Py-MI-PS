from PyMIPS.Datastructure.commands import *
from PyMIPS.Datastructure.immediate import Immediate, Ref_Immediate, StoredRefs


def test_li():
    num = Immediate(6)
    rp = RegisterPool.get_instance()
    t0 = rp.get_register("$t0")
    c = I_Type("li", target_register=t0, immediate=num)
    assert t0.get_contents() == 0
    f = li_command(c)
    assert t0.get_contents() == 0
    f()
    assert t0.get_contents() == 6


def test_lw():
    StoredRefs.store_ref("value", 12)
    ref = Ref_Immediate("value")
    rp = RegisterPool.get_instance()
    t3 = rp.get_register("$t3")
    c = I_Type("lw", t3, immediate=ref)
    assert t3.get_contents() == 0
    f = lw_command(c)
    assert t3.get_contents() == 0
    f()
    assert t3.get_contents() == 12


def test_add():
    rp = RegisterPool.get_instance()
    t4 = rp.get_register("$t4")
    t2 = rp.get_register("$t2")
    t3 = rp.get_register("$t3")
    c = R_Type("add", t4, t2, t3)
    t4.set_contents(lambda: 4)
    t3.set_contents(lambda: 4)
    t2.set_contents(lambda: 4)
    f = add_command(c)
    assert t4.get_contents() == 4
    assert t3.get_contents() == 4
    assert t2.get_contents() == 4
    f()
    assert t4.get_contents() == 8
    assert t3.get_contents() == 4
    assert t2.get_contents() == 4


def test_sw():
    rp = RegisterPool.get_instance()
    t5 = rp.get_register("$t5")
    t5.set_contents(lambda: 16)
    StoredRefs.store_ref("Z", 0)
    Z = Ref_Immediate("Z")
    c = I_Type("sw", t5, immediate=Z)
    f = sw_command(c)
    assert StoredRefs.get_ref("Z") == 0
    f()
    assert StoredRefs.get_ref("Z") == 16
