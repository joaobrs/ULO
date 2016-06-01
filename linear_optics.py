""" pete.shadbolt@gmail.com """

import itertools as it
import lomath


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

def polarization_qubit(i):
    return ("h%d" % i, "v%d" % i)

class Terry(Circuit):
    def build(self):
        """ Terry's circuit """
        for i in range(8):
            self.add(Photon("h%d" % i))

        for i in range(4):
            a, b = polarization_qubit(i), polarization_qubit(i+1)
            self.add(FusionII(a, b))

        self.add(FusionII("h1", "v1", "h2", "v2"))
        self.add(FusionII("h5", "v5", "h6", "v6"))
        self.add(FusionII("h2", "v2", "h5", "v5"))

        self.add(Herald("h1", "h2", "h5", "h6"))

