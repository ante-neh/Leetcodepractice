def getMinSum(arr, k):
    sum=0
    for i in range(k):
        sum+=arr[i]
    minSum=sum
    l=0
    for r in range(k,len(arr)):
        sum+=arr[r]
        sum-=arr[l]
        minSum=min(minSum,sum)
        l+=1
    return minSum