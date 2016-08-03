# -*- coding: utf-8 -*-

import numpy as np
from collections import defaultdict
from fractions import Fraction
from permanent import permanent

FACTORIAL = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800)

class State(defaultdict):
    def __init__(self, *args, **kwargs):
        super(State, self).__init__(complex, *args, **kwargs)

    def __str__(self):
        s = ""
        for label, amp in sorted(self.items()):
            if abs(amp)>1e-6:
                label = ", ".join(map(str, label))
                real_sign = " " if amp.real>=0 else "-"
                real_frac = Fraction(str(amp.real**2)).limit_denominator()
                imag_sign = "+" if amp.imag>=0 else "-"
                imag_frac = Fraction(str(amp.imag**2)).limit_denominator()
                bits = label, real_sign, real_frac, imag_sign, imag_frac
                s += "|{}〉: \t{}√{}\t{} i √{}\n".format(*bits)  #TODO: \rangle
        return s


def normalization(modes):
    """ Compute the normalization constant """
    table = defaultdict(int)
    for mode in modes:
        table[mode] += 1
    return np.prod([FACTORIAL[t] for t in table.values()])


def get_amplitudes(input_state, unitary, patterns):
    """ Simulates a given circuit, for a given input state, looking at certain terms in the output state """
    output_state = State()
    for cols, amplitude in input_state.items():
        cols = list(cols)
        n1 = normalization(cols)
        for rows in patterns:
            n2 = normalization(rows)
            perm = permanent(unitary[list(rows)][:, cols])
            value = amplitude * perm / np.sqrt(n1 * n2)
            output_state[rows] += value
    return output_state

def get_probabilities(input_state, unitary, patterns):
    """ Get probabilities"""
    output_state = get_amplitudes(input_state, unitary, patterns)
    return {key: np.abs(value) ** 2 for key, value in output_state.items()}

if __name__ == '__main__':
    s = State({(0,): 1})
    print s

