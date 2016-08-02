from ulo import simulator, Circuit, BS

def test_bs():
    c = BS()
    u = c.get_unitary()
    input = simulator.State({(0,):1})
    output = simulator.get_amplitudes(input, u, ((0,), (1,)))
    print output

