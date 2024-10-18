#we can use the def from the exe-2 too but there is an another way to solve it:
#total /avg of the rest*(first element+(total elements-1))
def avg(arr):
#base_case:
    if not arr :
        return None
    elif len(arr)== 1:
        return arr{0}
    else:
        return (arr[0] + (len(arr) -1 ) * avg(arr[1:]))/ len(arr)