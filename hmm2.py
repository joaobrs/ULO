
def bs(m1, m2):
    return "BS({},{})".format(m1, m2)

def bs2(h1, v1, h2, v2):
    return [bs(h1, h2),
            bs(h2, v2)]

def fii(h1, v1, h2, v2):
    return [bs(h1, v1),
            bs(h2, v2),
            bs(h1, h2),
            bs(v1, v2)]

class Polarization(object):
    def __init__(self, modes):
        for i, m in enumerate(modes):
            setattr(self, "{}{}".format("hv"[i%2], i/2), m)
        

def bell(*modes):
    m = Polarization(modes)
    print m
    return [fock(h1),
            fock(h2),
            fock(h3),
            fock(h4),
            fii(h1, v1, h2, v2),
            fii(h3, v3, h4, v4),
            bs2(h2, v2, h3, v3),
            herald(h2, h3, v2, v3)]



#print FII(0, 1, 2, 3)


#def BS(psi, m1, m2):
    #return psi + ["BS({},{})".format(m1, m2)]

#def BS2(psi, h1, v1, h2, v2):
    #return BS(BS(psi, h1, h2), v1, v2)

#def FII(psi, h1, v1, h2, v2):
    #return BS(

#print BS2([], "h1", "v1", "h2", "v2")

