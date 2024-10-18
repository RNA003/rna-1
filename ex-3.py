def reverse(arr,start=0,end=None):
   if end is None:
       end = len(arr)-1

   if start >= end:
      return arr

   arr[start],arr[end]=arr[end],arr [start]

   return reverse(arr,start+1,end-1)