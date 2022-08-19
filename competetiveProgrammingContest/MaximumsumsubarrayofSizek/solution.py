def getMaxSum(arr, k):
    sum=0
    maxsum=-100000   #the minimum value in the array to get this number see the constraint of the problem statement
    l=0
    for i in range(len(arr)):
        sum+=arr[i]
        if(i-l+1)==k:
            maxsum=max(maxsum,sum)
            sum-=arr[l]
            l+=1
    return maxsum

Input=[3, 5, 2, 1, 7]
k=2

print(getMaxSum(Input, k))