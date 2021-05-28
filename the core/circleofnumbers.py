def circleOfNumbers(n, firstNumber):
    a = n/2
    for i in range (n):
        if firstNumber<a:
            return (a+firstNumber)