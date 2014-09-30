import linear_optics as lo
from numpy import *
import os

def f(x):
    return y

P=10
M=20

# Get ready
circuit=lo.reck_scheme(M)
simulator=lo.simulator(circuit, nphotons=P)
print simulator.basis.hilbert_space_dimension
simulator.set_input_state(range(P))
phases = random.uniform(0, pi*2, len(circuit.phaseshifters))
circuit.set_phases(phases)

# Go
number_of_terms=1000
print simulator.get_output_state()

