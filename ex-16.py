def sub(num):

    result =[]
    def track(start,curr):
        result.append(curr.copy())
        for i in range (start,len(num)):
            curr.append(num[i])
            track(i+1,curr)
            curr.pop()

        track(0,[])
        return result