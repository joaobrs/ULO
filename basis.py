 #!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import itertools as it


class Naming():

    def __str__(self):
        terms = "\n".join("{}: {}".format(i, self.fwd(i)) for i in range(3))
        return "Naming:\n{}\n...".format(terms)


class Path(Naming):

    def fwd(self, index):
        return "m{}".format(index)

    def back(self, name):
        return int(name[1:])


class Polarization(Naming):

    def fwd(self, index):
        return "{}{}".format("HV"[index%2], index/2)

    def back(self, name):
        return int(name[1:])*2 + (name[0] == "H")

if __name__ == '__main__':
    # l = Label(0, "H0")
    n = Path()
    print n

