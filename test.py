from pprint import pprint
import linear_optics as lo
import numpy as np

def test():
    circuit = [{'type': 'source', 'x': 0, 'y': 0},
        {'type': 'source', 'x': 0, 'y': 1},
      {'type': 'coupler', 'x': 1, 'y': 0, 'ratio': 0.5},
      {'type': 'coupler', 'x': 1, 'y': 10, 'ratio': 0.5}]

    circuit = lo.compile(circuit)
    output_state = lo.simulate(**circuit)

    for key, value in sorted(output_state.items(), key=lambda x:x[0]):
        if abs(value)>0: print "|%s> : %s" % (key, value)

if __name__=="__main__":
    test()
