import numpy as np
from ulo import Circuit

def test_circuit():
    c = Circuit(name="Test circuit")
    assert c.name == "Test circuit"

def test_dynamic_beamsplitter():
    def beamsplitter_unitary(reflectivity):
        return "ubs({})".format(reflectivity)
    
    #Beamsplitter = Circuit(name="Beamsplitter", unitary = np.eye(2))
    #print Beamsplitter.get_unitary()
    Beamsplitter = Circuit(name="Beamsplitter", unitary = beamsplitter_unitary)
    print Beamsplitter(0, reflectivity=.69).get_unitary()
    #Beamsplitter = Circuit(name="Beamsplitter", unitary = beamsplitter_unitary(.5))

    #Beamsplitter(5, reflectivity=.1)


