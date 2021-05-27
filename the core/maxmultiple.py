def maxMultiple(divisor, bound):
    N = divisor
    for i in range(bound):
        if (N%divisor > 0):
            return N
        N = N + 1