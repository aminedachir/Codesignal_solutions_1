def lateRide(n):
    for i in range(n):
        if n==0:
            return n
        else:
            mint = math.floor(n/60)
            c = n-mint * 60
            a = mint/10 + mint%10
            b = c/10 + c%10
            return int(a)+int(b)