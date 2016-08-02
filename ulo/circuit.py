"""
Here we implement a Circuit object which describes linear-optical circuits.

.. todo::

    Polarization is going to be a **layer on top of this**.

.. todo::

    Decide between relative and absolute mode labels

"""

import itertools as it
from fractions import Fraction

class Circuit(object):

    """ A circuit """

    components = []

    def __init__(self, *modes, **kwargs):
        self.modes = modes

    def decompose(self, modes=None):
        """ Get the unitary matrix of this circuit """
        remapped = [modes[i] for i in self.modes] if modes else self.modes
        return it.chain(*(c.decompose(remapped) for c in self.components))

    def get_unitary(self):
        return [(u, modes) for u, modes in self.decompose()]

    def set_parameter(self, key, values):
        """ Will go and set all the reflectvities, phases, etc """
        values = it.cycle(values)
        for c in self.components:
            c.set_parameter(key, values)

    def __str__(self):
        s = "{} {}".format(self.__class__.__name__, self.modes)
        for thing in self.components:
            for line in str(thing).split("\n"):
                s += "\n.  " + line
        return s


class Component(Circuit):
    def decompose(self, modes=None):
        remapped = [modes[i] for i in self.modes] if modes else self.modes
        return ((self.get_unitary(), remapped),)

    def set_parameter(self, key, values):
        if hasattr(self, key):
            setattr(self, key, values.next())

class Beamsplitter(Component):
    """ A simple beamsplitter """

    reflectivity = 0.5

    def get_unitary(self):
        return "bsu {}".format(self.reflectivity)

    def __str__(self):
        rf = Fraction(str(self.reflectivity)).limit_denominator()
        return "Beamsplitter {}, reflectivity = {}".format(self.modes, rf)


class Phase(Component):
    """ A phase shifter """

    phi = 0

    def get_unitary(self):
        return "phase"

    def __str__(self):
        ph = Fraction(str(self.phi/np.pi)).limit_denominator()
        return "Phase {}, phi = {} pi".format(self.modes, ph)


class Swap(Component):

    """ Swaps two modes -- easy to make a PBS like this """

    def get_unitary(self):
        return "swpu"


class BSPair(Circuit):

    """ A pair of beamsplitters """
    components = [Beamsplitter(0, 1), Beamsplitter(2, 3)]


class Fusion(Circuit):

    """ A fusion gate """
    components = [BSPair(0, 1, 2, 3), Swap(1, 2), BSPair(0, 1, 2, 3)]


class TwoFusions(Circuit):

    """ Two fusion gates """
    components = [Fusion(0, 1, 2, 3), Fusion(4, 5, 6, 7)]


class MZI(Circuit):

    """ A Mach-Zehnder interferometer, testing parametric circuits """
    components = [Phase(0), Beamsplitter(0), Phase(0), Beamsplitter(0), Phase(0)]

if __name__ == '__main__':
    class Test(Circuit):
        components = [Beamsplitter(0), Beamsplitter(1)]

    t = Test()
    t.set_parameter("reflectivity", [.69, .5])
    print t.get_unitary()

    c = TwoFusions()
    print c

