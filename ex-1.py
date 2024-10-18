def divis(a,b):

    if a<b:
        return 0
    else:
        return 1 + divis(a-b,b)