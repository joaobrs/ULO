import numpy as np
from permanent import permanent

ir2 = 1 / np.sqrt(2)
factorial = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800)

def choose(n, k):
    return 0 if n < k else int(np.prod([(i + k) / i for i in range(1, n - k + 1)]) + .5)
