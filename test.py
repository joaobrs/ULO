from pprint import pprint
import linear_optics as lo
import numpy as np

circuit = [{'type': 'bellpair', 'pos': {'x': 0, 'y': 0}},
  {'type': 'sps', 'pos': {'x': 0, 'y': 5}},
  {'type': 'phaseshifter', 'pos': {'x': 2, 'y': 0}, 'phase':0},
  {'type': 'coupler', 'pos': {'x': 2, 'y': 1}, 'ratio': 0.5},
  {'type': 'coupler', 'pos': {'x': 3, 'y': 1}, 'ratio': 0.5},
  {'type': 'crossing', 'pos': {'x': 2, 'y': 3}},
  {'type': 'crossing', 'pos': {'x': 4, 'y': 4}}]

circuit = lo.compile_circuit(circuit)
output_state = lo.simulate(**circuit)

print "\nOutput state:"
for key, value in sorted(output_state.items(), key=lambda x:x[0]):
    if abs(value)>0: print "|%s> : %.2f" % (key, abs(value))

