def facto(n):

    def fact(num):


        if num==0:
            return 1
        else:
            return num*fact(num-1)

    sum=0
    for i in range(1,n+1):
        sum +=1/fact(i)
    return sum