def getMinMaxDiff(nums, k):
    currentSum=0
    for i in range(k):
        currentSum+=nums[i]
    maxSum=currentSum/k
    minSum=currentSum/k
    l=0
    for r in range(k,len(nums)):
        currentSum+=nums[r]
        currentSum-=nums[l]
        maxSum=max(maxSum,currentSum/k)
        minSum=min(currentSum/k,minSum)
        l+=1
    return maxSum-minSum
arr=[3, 8, 9, 15]
k= 2
print(getMinMaxDiff(arr, k))
#time complexity O(n)
#space complexity O(1)