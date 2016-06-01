""" pete.shadbolt@gmail.com """

import itertools as it
from permanent import permanent
import numpy as np

ir2 = 1 / np.sqrt(2)
factorial = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800)

def choose(n, k):
    return 0 if n < k else int(np.prod([(i + k) / i for i in range(1, n - k + 1)]) + .5)

class State(dict):

    def __init__(self, basis):
        """ A sparse quantum state """
        self.basis = basis
        dict.__init__(self)

    def __str__(self):
        """ For printout """
        return "\n".join("|{}> : {}".format(key, value)
                for key, value in self.terms.items())
            
class Gate(object):

    def __init__(self, input_modes, output_modes=None, parameters=None):
        self.input_modes = input_modes
        self.output_modes = output_modes if input_modes else input_modes
        self.parameters = parameters
        self.components = []


class Basis(object):

    def __init__(self, p, m):
        self.nphotons = p
        self.nmodes = m
        self.d = choose(m + p - 1, p)

    def get(self, index):
        try:
            return tuple(int(i) for i in index)
        except TypeError:
            return int(index)

    def __str__(self):
        return "Basis:\n{}".format("\n".join(map(str, term for term in self)))

class Herald(object):
    def __init__(self, terms):
        self.terms = terms

    def __str__(self):
        return "Herald: {}".format(self.terms)


class Circuit(object):

    def __init__(self):
        self.components = []
        self.basis = Basis()
        self.build()

    def add(self, thing, address):
        """ Add a component to the circuit """
        self.components.append(thing(self.basis.get(address)))

    def build(self):
        """ Build the circuit """
        pass


class Terry(Circuit):
    basis = PolarizationBasis(8)

    def build(self):
        """ Terry's circuit """
        for i in range(8):
            self.add(Photon, ("0h"))

        for i in range(4):
            self.add(FusionII, (i, i + 1))

        self.add(FusionII, (1, 2))
        self.add(FusionII, (5, 6))
        self.add(FusionII, (2, 5))

        self.add(Herald, ("1h", "2h", "5h", "6h"))

