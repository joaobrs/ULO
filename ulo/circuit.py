"""
This module implements the ``Circuit`` class, which is used to model linear-optical circuits.

It doesn't care about input states or output states -- it's just used to build and parametrize interferometers.

.. todo::

    Polarization is going to be a **layer on top of this**.

.. todo::

    Decide between relative and absolute mode labels

"""

import itertools as it
from fractions import Fraction
import numpy as np


class Circuit(object):

    """ The Circuit class is the basis of ``ulo``'s approach to constructing linear optical circuits. """

    components = []

    def __init__(self, *modes, **kwargs):
        self.modes = modes

    def decompose(self, modes=None):
        """ Decomposes the circuit into a simple list of ``Component``s::

        :param modes: Should not be used

            >>> print c.decompose()

        """
        remapped = [modes[i] for i in self.modes] if modes else self.modes
        return it.chain(*(c.decompose(remapped) for c in self.components))

    def get_unitary(self):
        """ Get the unitary matrix representing this circuit. """
        modes = set(it.chain(*(m for n, u, m in self.decompose()))) | set(
            self.modes)  # TODO: sux
        output = np.eye(len(modes), dtype=complex)
        for n, u, m in self.decompose():
            output[list(m)] = np.dot(u, output[list(m)])
        return output

    def show_decomposition(self):
        """ Useful to check decompositions """
        print "\n".join("{} {}".format(n, m) for n, u, m in self.decompose())

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

    """ A ``Component`` is a ``Circuit`` with a specified unitary representation -- it is not a composite object.
    """

    def decompose(self, modes=None):
        remapped = tuple([modes[i]
                         for i in self.modes] if modes else self.modes)
        return ((self.__class__.__name__, self.get_unitary(), remapped),)

    def set_parameter(self, key, values):
        if hasattr(self, key):
            setattr(self, key, values.next())


class Beamsplitter(Component):

    """ A simple beamsplitter """

    ratio = 0.5

    def get_unitary(self):
        r = 1j * np.sqrt(self.ratio)
        t = np.sqrt(1 - self.ratio)
        return np.array([[t, r], [r, t]])

    def __str__(self):
        rf = Fraction(str(self.ratio)).limit_denominator()
        return "Beamsplitter {}, ratio = {}".format(self.modes, rf)

BS = Beamsplitter


class Phase(Component):

    """ A phase shifter """

    phi = 0

    def get_unitary(self):
        return np.array([[np.exp(1j * self.phi)]])

    def __str__(self):
        ph = Fraction(str(self.phi / np.pi)).limit_denominator()
        return "Phase {}, phi = {} pi".format(self.modes, ph)


class Swap(Component):

    """ Swaps two modes -- easy to make a PBS like this """

    def get_unitary(self):
        return np.array([[0, 1], [1, 0]], dtype=complex)


class BSPair(Circuit):

    """ A pair of beamsplitters """
    components = BS(0, 1), BS(2, 3)


class FusionI(Circuit):

    """ A fusion gate (#TODO: this is wrong) """
    components = BS(0, 1), Swap(1, 2), BSPair(0, 1, 2, 3)


class FusionII(Circuit):

    """ A fusion gate """
    components = BSPair(0, 1, 2, 3), Swap(1, 2), BSPair(0, 1, 2, 3)


class TwoFusionsII(Circuit):

    """ Two fusion gates """
    components = FusionII(0, 1, 2, 3), FusionII(4, 5, 6, 7)


class MZI(Circuit):

    """ A Mach-Zehnder interferometer, testing parametric circuits """
    components = Phase(0), BS(0), Phase(0), BS(0), Phase(0)


