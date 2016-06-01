from basis import *

def test_label():
    """ Test that labels work okay """
    l = Label(0, "H0")
    assert str(l) == "H0"
    assert int(l) == 0

def _test_naming():
    """ Test that our naming is good """
    n = Naming(5)
    assert len(n)==5
    assert Label(0, "m0") in n

def test_basis():
    assert mode("m0") == 0
    assert mode(0) == 0
    assert polarization("h0") == 0

