def getCountNegatives(arr, k):
    result=[]
    l,counter=0,0
    for r in range(len(arr)):
        if arr[r]<0:
            counter+=1
        if (r-l+1)==k:
            result.append(counter)
            if arr[l]<0:
                counter-=1
            l+=1
    return result
#time complexity O(n)
#space complexity O(1)

