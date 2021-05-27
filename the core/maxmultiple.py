def maxMultiple(divisor, bound):
    N = 0
    for i in range(bound):
        if (N%divisor < 0):
            return N
        else:
            N = bound - 1