def circleOfNumbers(n, firstNumber):
    a = n/2 + firstNumber
    if n<=10:
        if a<10:
            return a
        elif a>10:
            a = a-10
            return a
    elif n>10:
        return (n/4 + firstNumber)