def candies(n, m):
    for i in range(m):
        a = m%n
        if a > 0:
            m = m - 1
            a = m%n
            if a == 0:
                return m
        elif m<n:
            return 0
        else:
            return m