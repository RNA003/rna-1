def mainchange(amo,den=[10,5,2]):


    def changee(amo,ind,curr):
        if amo ==0:
            print(curr)
            return
        if amo <0 or ind >= len(den):
            return
        coin=den[ind]
        for i in range(amo//coin+1):
            changee(amo-i*coin,ind+1,curr+[i*coin])
    changee(amo,0,[])