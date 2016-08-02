
class Circuit(object):
    def __init__(self, *things, **kwargs):
        self.things = things
        self.name = kwargs.get("name", "Unnamed")
        self.unitary = kwargs.get("unitary", None)
        self.position = kwargs.get("position", None)

    def __call__(self, *position, **kwargs):
        return Circuit(*self.things, name=self.name, unitary=self.unitary, position=position)

    def __str__(self):
        s = "{}: (modes: {})".format(self.name, self.position)
        for thing in self.things:
            for line in str(thing).split("\n"):
                s += "\n.   "+line
        return s


    
if __name__ == '__main__':
    # All of the following should run!
    Beamsplitter = Circuit(name="Beamsplitter", unitary="Ubs")

    Swap = Circuit(name="Swap", unitary="Uswap")

    TwoBS = Circuit(Beamsplitter(0, 1), Beamsplitter(2, 3), name="Beamsplitter pair")
    Fusion = Circuit(TwoBS(0,1,2,3), Swap(1, 2), TwoBS(0, 1, 2, 3), name="Type-II fusion")

    print Fusion
    print Fusion()
    print Fusion(1)


    # All of the following should run!
    # Polarization encoding
    #Fusion = Circuit(HWP(0), HWP(1), PBS(0, 1), HWP(0), HWP(1))

    # Path encoding
    #Fusion = Circuit(BS(0, 1), BS(2, 3), Map((1, 2), (2, 1)), BS(0, 1), BS(2, 3))
    #Fusion = Circuit(BS(0, 1), BS(2, 3), Map((1, 2), (2, 1)), BS(0, 1), BS(2, 3))

    #TwoFusions = Circuit(Fusion(0, 1), Fusion(2, 3))
    #TwoFusions = Circuit(Fusion(0, 1, 2, 3), Fusion(2, 3, 4, 5))

    
