class Circuit(object):
    def __init__(self, name, *things, **kwargs):
        self.name = name
        self.things = things
        self.unitary = kwargs.get("unitary", None)
        self.position = kwargs.get("position", None)

    def __call__(self, *position, **kwargs):
        return Circuit(self.name, *self.things, position=position)

    def __str__(self):
        return "{} ({}), pos={}".format(self.name, ", ".join(map(str, self.things)), self.position)


    
if __name__ == '__main__':
    # All of the following should run!
    BS = Circuit("BS", unitary="U")
    print BS
    print BS.unitary
    Fusion = Circuit("Fusion", BS(0), BS(1))
    print Fusion
    print Fusion()
    TwoFusions = Circuit("TwoFusions", Fusion(0, 1), Fusion(1, 2))
    print TwoFusions
    #print Fusion(1)


    #print Circuit(HWP(0))

    # Polarization encoding
    #Fusion = Circuit(HWP(0), HWP(1), PBS(0, 1), HWP(0), HWP(1))

    # Path encoding
    #Fusion = Circuit(BS(0, 1), BS(2, 3), Map((1, 2), (2, 1)), BS(0, 1), BS(2, 3))
    #Fusion = Circuit(BS(0, 1), BS(2, 3), Map((1, 2), (2, 1)), BS(0, 1), BS(2, 3))

    #TwoFusions = Circuit(Fusion(0, 1), Fusion(2, 3))
    #TwoFusions = Circuit(Fusion(0, 1, 2, 3), Fusion(2, 3, 4, 5))

    
