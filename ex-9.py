def facto(n):
    if n==0:
        return 1
    else:
        return fact(n) + facto(n-1)
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)