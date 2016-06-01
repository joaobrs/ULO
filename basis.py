 #!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import itertools as it

def choose(n, k):
    return 0 if n < k else int(np.prod([(i + k) / i for i in range(1, n - k + 1)]) + .5)

class Label(object):
    def __init__(self, mode, name=None):
        self.mode = mode
        self.name = name if name else "m{}".format(mode)

    def __str__(self):
        return "{}".format(self.name)

    def __int__(self):
        return self.mode

class Naming(list):
    def __init__(self):
        terms = (Label(i, self.get(i)
        list.__init__(terms)

    def __str__(self):
        return "Naming: " + ", ".join(str(x) for x in self)

class PathNaming(Naming):
    def get(self, index):
        return "m{}".format(index)

class PolarizationNaming(Naming):
    def get(self, index):
        return "{}{}".format("HV"[index%2], index/2)

class Basis(object):

    def __init__(self, p, m):
        self.nphotons = p
        self.nmodes = m
        self.d = choose(m + p - 1, p)

    def get(self, index):
        try:
            return tuple(int(i) for i in index)
        except TypeError:
            return int(index)

    def terms(self):
        """ Iterate over terms in this basis """
        return it.combinations_with_replacement(xrange(self.nmodes), self.nphotons)


    def __str__(self):
        pass
        #return "|{}⟩".format(self.name.upper())
        #return "Basis:\n{}".format("\n".join(map(str, (term for term in self.terms()))))



