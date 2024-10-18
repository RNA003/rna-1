def findmax(arr,low,high):
#base case:
    if low == high:
        return arr[low]

    mid = (low + high ) // 2

    max_left=findmax(arr,low,mid)
    max_right=findmax(arr,mid+1,high)

    return max(max_left,max_right)
