import linear_optics as lo
from numpy import *
import os

P=8
M=8

# Get ready
circuit=lo.reck_scheme(M)
simulator=lo.simulator(circuit, nphotons=P)
print simulator.basis.hilbert_space_dimension
simulator.set_input_state(range(P))
phases = random.uniform(0, pi*2, len(circuit.phaseshifters))
circuit.set_phases(phases)

# Go
number_of_terms=12000
patterns=[random.randint(0, M, P) for i in range(number_of_terms)]
probs = simulator.get_probabilities(patterns=patterns).round(4)
print sum(probs)
