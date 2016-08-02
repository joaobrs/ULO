class Circuit(object):
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


class Beamsplitter(Circuit):
    """ A simple beamsplitter """

    def get_unitary(self, modes):
        return ["bsu({}) @ {}".format(self.args.get("reflectivity", .5), modes)]


class Swap(Circuit):
    """ Swaps two modes -- easy to make a PBS like this """

    def get_unitary(self, modes):
        return ["swpu() @ {}".format(modes)]


class BSPair(Circuit):
    components = [Beamsplitter(0, 1), Beamsplitter(2, 3)]


class Fusion(Circuit):
    components = [BSPair(0, 1), Swap(1, 2), BSPair(2, 3)]


class TwoFusions(Circuit):
    components = [Fusion(0, 1, 2, 3), Fusion(4, 5, 6, 7)]

if __name__ == '__main__':
    c = TwoFusions()
    print c
    print c.get_unitary()

