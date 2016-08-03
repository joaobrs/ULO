import numpy as np
from ulo import Circuit, BS, FusionII

def test_circuit():
    """ Simple tests """
    c = Circuit(0, 1)
    assert str(c) == "Circuit (0, 1)"
    assert c.modes == (0, 1)
    assert list(c.decompose()) == []
    assert np.allclose(c.get_unitary(), np.eye(2))


def test_bs():
    """ Beamsplitter tests """
    b = BS()
    target = np.array([[1, 1j], [1j, 1]])/np.sqrt(2)
    assert np.allclose(b.get_unitary(), target)

    b.ratio = 0
    assert np.allclose(b.get_unitary(), np.eye(2))


def test_fusion():
    """ Test that fusion makes sense """
    c = FusionII()
    u = c.get_unitary()
    assert np.allclose(np.dot(np.transpose(np.conjugate(u)), u), np.eye(4)), "Fusion is unitary"


