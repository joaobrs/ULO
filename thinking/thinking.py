
class Circuit(object):

    def __init__(self, *things, **kwargs):
        self.things = things
        self.name = kwargs.get("name", "Unnamed")
        self.unitary = kwargs.get("unitary", None)
        self.modes = kwargs.get("modes", None)

    def __call__(self, *modes, **kwargs):
        return Circuit(*self.things, name=self.name, unitary=self.unitary, modes=modes)

    def __str__(self):
        s = "{} @ {}".format(self.name, ", ".join(map(str, self.modes)))
        for thing in self.things:
            for line in str(thing).split("\n"):
                s += "\n.   " + line
        return s

    def get_unitary(self, modes=None):
        """ Get the unitary matrix for this circuit """
        #print "getting unitary for {} {} {}".format(self.name, self.modes, modes)
        if self.unitary:
            #print modes, self.modes
            return ["{} @ {}".format(self.unitary, ", ".join(str(modes[i]) for i in self.modes))]
        else:
            pieces = []
            for thing in self.things:
                pieces += thing.get_unitary([modes[i] for i in self.modes] if modes else self.modes)
            return pieces


if __name__ == '__main__':
    # All of the following should run!
    Beamsplitter = Circuit(name="Beamsplitter", unitary="Ubs")

    Swap = Circuit(name="Swap", unitary="Uswap")

    TwoBS = Circuit(Beamsplitter(0, 1),
                    Beamsplitter(2, 3), name="Beamsplitter pair")
    Fusion = Circuit(TwoBS(0, 1, 2, 3), Swap(
        1, 2), TwoBS(0, 1, 2, 3), name="Type-II fusion")

    print Fusion(4, 5, 6, 7).get_unitary()

    TwoFusions = Circuit(
            Fusion(0, 1, 2, 3), 
            Fusion(4, 5, 6, 7), 
            name="A pair of fusion gates")
    print TwoFusions(*range(8))
    print TwoFusions(*range(8)).get_unitary()


    # All of the following should run!
    # Polarization encoding
    # Fusion = Circuit(HWP(0), HWP(1), PBS(0, 1), HWP(0), HWP(1))

    # Path encoding
    # Fusion = Circuit(BS(0, 1), BS(2, 3), Map((1, 2), (2, 1)), BS(0, 1), BS(2, 3))
    # Fusion = Circuit(BS(0, 1), BS(2, 3), Map((1, 2), (2, 1)), BS(0, 1),
    # BS(2, 3))

    # TwoFusions = Circuit(Fusion(0, 1), Fusion(2, 3))
    # TwoFusions = Circuit(Fusion(0, 1, 2, 3), Fusion(2, 3, 4, 5))
