#after run this code we would have the answer
def ack(m,n):
    if m<0 or n<0:
        return 0
    elif m==0:
        return n+1
    elif n==0:
        return ack(m-1,1)
    else:
        return ack(m-1,ack(m,n-1))
result= ack(3,2)
print(result)