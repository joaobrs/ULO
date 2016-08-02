def HWP(*modes):
    return "hwp {}".format(modes)

def Circuit(stuff):
    return stuff

    
if __name__ == '__main__':
    # All of the following should run!
    print Circuit(HWP(0))

    # Polarization encoding
    Fusion = Circuit(HWP(0), HWP(1), PBS(0, 1), HWP(0), HWP(1))

    # Path encoding
    Fusion = Circuit(BS(0, 1), BS(2, 3), Map((1, 2), (2, 1)), BS(0, 1), BS(2, 3))
    Fusion = Circuit(BS(0, 1), BS(2, 3), Map((1, 2), (2, 1)), BS(0, 1), BS(2, 3))

    TwoFusions = Circuit(Fusion(0, 1), Fusion(2, 3))
    TwoFusions = Circuit(Fusion(0, 1, 2, 3), Fusion(2, 3, 4, 5))

    
