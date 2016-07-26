

class Circuit(object):
    def __init__(self):
        self.basis = ModeBasis()


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

