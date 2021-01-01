def factorial(n):
    if n<1:
        return(1)
    if n >=1 and n<=100:
        s = n
        s = s* factorial(n-1)
        return(s)

