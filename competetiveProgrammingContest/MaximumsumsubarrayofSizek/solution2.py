def getMaxSum(arr, k):
    sum=0
    for i in range(k):
        sum+=arr[i]
    maxSum,l=sum,0
    for r in range(k,len(arr)):
        sum+=arr[r]
        sum-=arr[l]
        maxSum=max(maxSum,sum)
        l+=1
    return maxSum
