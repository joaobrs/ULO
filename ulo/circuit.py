"""
Here we implement a Circuit object which describes linear-optical circuits.

.. todo:: 

    Polarization is going to be a **layer on top of this**.

.. todo:: 

    Decide between relative and absolute mode labels

"""

class Circuit(object):
    """ A circuit """
    
    components = []

    def __init__(self, *modes, **kwargs):
        self.modes = modes
        self.args = kwargs

    def __str__(self):
        s = "{} {} {}".format(self.__class__.__name__, self.modes, self.args)
        for thing in self.components:
            for line in str(thing).split("\n"):
                s += "\n.  " + line
        return s

    def get_unitary(self, modes = None):
        remapped = [modes[i] for i in self.modes] if modes else self.modes
        pieces = []
        for component in self.components:
            pieces += component.get_unitary(remapped)
        return pieces

    def set_parameter(self, key, values):
        """ Will go and set all the reflectvities, phases, etc """
        values = values if iterable(values) else (value for component in self.components)
        for component, value in zip(self.components):
            component.args[key] = value


class Beamsplitter(Circuit):
    """ A simple beamsplitter """

    def get_unitary(self, modes):
        return ["bsu({}) @ {}".format(self.args.get("reflectivity", .5), modes)]


class Swap(Circuit):
    """ Swaps two modes -- easy to make a PBS like this """

    def get_unitary(self, modes):
        return ["swpu() @ {}".format(modes)]


class BSPair(Circuit):
    """ A pair of beamsplitters """
    components = [Beamsplitter(0, 1), Beamsplitter(2, 3)]


class Fusion(Circuit):
    """ A fusion gate """
    components = [BSPair(0, 1), Swap(1, 2), BSPair(2, 3)]


class TwoFusions(Circuit):
    components = [Fusion(0, 1, 2, 3), Fusion(4, 5, 6, 7)]

class MZI(Circuit):
    components = [Phase(0), Beamsplitter(0), Phase(0), Beamsplitter(0), Phase(0)]

if __name__ == '__main__':
    c = TwoFusions()
    print c
    print c.get_unitary()

