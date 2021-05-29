def lateRide(n):
    h = math.floor(n/60)
    mint = n / 60
    return math.floor(h/ 10) + (h % 10) + math.floor(mint / 10) + (mint % 10)
