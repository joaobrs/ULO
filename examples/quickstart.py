from ulo import Circuit, BS, Swap, State, get_amplitudes

class FusionII(Circuit):
    components = [BS(0, 1), BS(2, 3), Swap(1, 2), BS(0, 1), BS(2, 3)]

circuit = FusionII()
print circuit

state = State({(0, 1, 2, 3): 1})
print state

u = circuit.get_unitary()
print u

print get_amplitudes(state, u, ((0, 1, 2, 3),))
