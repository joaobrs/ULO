"""
Here we implement a Circuit object which describes linear-optical circuits.

.. todo::

    Polarization is going to be a **layer on top of this**.

.. todo::

    Decide between relative and absolute mode labels

"""

import itertools as it

class Circuit(object):

    """ A circuit """

    components = []

    def __init__(self, *modes, **kwargs):
        self.modes = modes
        self.args = kwargs

    def decompose(self, modes=None):
        """ Get the unitary matrix of this circuit """
        remapped = [modes[i] for i in self.modes] if modes else self.modes
        return it.chain(*(c.decompose(remapped) for c in self.components))

    def get_unitary(self):
        return [(u, modes) for u, modes in self.decompose()]

    def set_parameter(self, key, values):
        """ Will go and set all the reflectvities, phases, etc """
        values = values if iterable(values) else (
            value for component in self.components)
        for component, value in zip(self.components):
            component.args[key] = value

    def __str__(self):
        s = "{} {} {}".format(self.__class__.__name__, self.modes, self.args)
        for thing in self.components:
            for line in str(thing).split("\n"):
                s += "\n.  " + line
        return s


class Component(Circuit):
    def decompose(self, modes=None):
        remapped = [modes[i] for i in self.modes] if modes else self.modes
        return ((self.get_unitary(**self.args), remapped),)

class Beamsplitter(Component):

    """ A simple beamsplitter """

    def get_unitary(self):
        return "bsu"


class Phase(Component):

    """ A phase shifter """

    def get_unitary(self):
        return "phase"


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
    components = [Phase(0), Beamsplitter(
        0), Phase(0), Beamsplitter(0), Phase(0)]

if __name__ == '__main__':
    c = TwoFusions()
    print c.get_unitary()
    #print list(c.decompose())
    #for u, m in c.decompose():
        #print u, m

