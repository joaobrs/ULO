""" Trying out second quantization """
from math import *
ir2 = 1/sqrt(2)

def swap(m1, m2, state):
    for key, value in state:
        key.replace(m1, m2)
        key.replace(m2, m1)

def bs(m1, m2, state):
    pass  

def pprint(state):
    for key, value in state:
        print "|%s> \t %f" % (",".join(map(str,key)), value)

state = [["abf", ir2], ["cdf", ir2]]
swap(5,6,state)
#pprint(state)

