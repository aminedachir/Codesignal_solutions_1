def circleOfNumbers(n, firstNumber):
    a = n/2 + firstNumber
    if n<=10:
        if a<10:
            return a
        elif a>10:
            a = a-10
            return a
    elif 15<n<20:
        return (n/2 + firstNumber)
    
    elif n>10<15:
        return n/3
        
    elif n==6:
        return (n/4 - firstNumber)