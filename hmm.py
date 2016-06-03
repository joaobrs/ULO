import numpy as np


class Primitive(object):

    def __init__(self, inputs, outputs=None):
        self.inputs = inputs
        self.outputs = outputs if outputs else inputs


class Beamsplitter(object):

    def __init__(self, inputs, outputs=None, reflectivity=0.5):
        self.inputs = inputs
        self.outputs = outputs if outputs else inputs
        self.unitary = np.array([[1, 1j], [1j, 1]]) / np.sqrt(2)

class Mapping(object):

    def __init__(self, *mapping):
        self.mapping = mapping
        # NOT eye. it should just act on the space.
        self.unitary = np.eye(len(mapping), dtype=complex)




class FusionII(Circuit):
    def build(self):
        self.add(Beamsplitter(0, 1),
                 Beamsplitter(2, 3),
                 Mapping((1, 2)),
                 Beamsplitter(0, 1),
                 Beamsplitter(2, 3))

    def get_unitary()
        U = np.eye(maxd, dtype=complex)
        for c in self.components:
            u  = translate(c)
            U *= u


f = FusionII()








# class Component(object):
    # def __init__(self):
        # self.inputs = []
        # self.outputs = []

    # def __str__(self):
        # return "Component: {} {}".format(self.inputs, self.outputs)

# class Beamsplitter(Component):
    # def __init__(self, ratio=.5):
        # self.inputs = [0, 1]
        # self.outputs = [0, 1]

    # def get_unitary(self):
        # return np.matrix([[1,1j],[1j,1]]) / np.sqrt(2)

# class FusionII(Component):
    # def __init__(self, ):
        # self.nodes = [Beamsplitter(), Beamsplitter(), Beamsplitter(), Beamsplitter()]
        # self.

# b = Beamsplitter()
