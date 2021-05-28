def maxMultiple(divisor, bound):
    N = bound
    i = 0
    while (i < bound):
        if (N%divisor == 0):
            return N
        else:
            N = N - 1