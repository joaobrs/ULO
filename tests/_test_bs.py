import linear_optics as lo
from numpy import pi, allclose

sps = [{"type": "fockstate", "x": 0, "y": 0, "n": 1}]
pairsource = [{"type": "fockstate", "x": 0, "y": 0, "n": 1},
              {"type": "fockstate", "x": 0, "y": 1, "n": 1}]


def mzi(phase):
    """ Helper to generate MZIs """
    return [{"type": "coupler", "x": 1, "y": 0, "ratio": 0.5},
            {"type": "phaseshifter", "x": 2, "y": 0, "phase": phase},
            {"type": "coupler", "x": 3, "y": 0, "ratio": 0.5}]


def test_mzi():
    """ Test MZIs """
    circuit = sps + mzi(0)
    probabilities = lo.get_probabilities(**lo.compile(circuit))
    assert allclose(probabilities[(0,)], 0)
    assert allclose(probabilities[(1,)], 1)

    circuit = sps + mzi(pi / 2)
    probabilities = lo.get_probabilities(**lo.compile(circuit))
    assert allclose(probabilities[(0,)], .5)
    assert allclose(probabilities[(1,)], .5)


def test_hom_dip():
    """ Test HOM dips """
    circuit = pairsource + mzi(pi / 2)
    probabilities = lo.get_probabilities(**lo.compile(circuit))
    assert allclose(probabilities[(0, 1)], 0)

    circuit = pairsource + mzi(0)
    probabilities = lo.get_probabilities(**lo.compile(circuit))
    assert allclose(probabilities[(0, 1)], 1)


def test_readme():
    """ Example from the README """
    phase = pi / 2
    pairsource = [{"type": "fockstate", "x": 0, "y": 0, "n": 1},
                  {"type": "fockstate", "x": 0, "y": 1, "n": 1}]
    mzi = [{"type": "coupler", "x": 1, "y": 0, "ratio": 0.5},
           {"type": "phaseshifter", "x": 2, "y": 0, "phase": phase},
           {"type": "coupler", "x": 3, "y": 0, "ratio": 0.5}]

    circuit = sps + mzi
    compiled_circuit = lo.compile(circuit)
    amplitudes = lo.get_amplitudes(**compiled_circuit)
    probabilities = lo.get_probabilities(**compiled_circuit)
