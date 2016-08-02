import numpy as np
from ulo import Circuit

def bsu(reflectivity):
    """ Used for testing """
    return "bsu({})".format(reflectivity)

def test_circuit():
    c = Circuit(name="Test circuit")
    assert c.name == "Test circuit"

def test_dynamic_beamsplitter():
    """ This is a really wierd way of programming. Who can say if it is good? """
    Beamsplitter = Circuit(name="Beamsplitter", unitary=bsu)
    assert Beamsplitter(0, reflectivity="test").get_unitary() == ["bsu(test) @ 0"]

class Circuit:

class BeamSplitter(circuit):
    def __init__(self, reflectivity):
        self.unitary = 

class Fusion(Circuit):
    components = [
            DualBeamsplitter(1, 2, 3, 4), 
            Swap(2, 3),
            DualBeamsplitter(1, 2, 3, 4), 
    ]


