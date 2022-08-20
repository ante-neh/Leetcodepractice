def getMinMaxDiff(nums, k):
    currentSum=0
    maxSum=-100000
    minSum=float("inf")
    l=0
    for r in range(len(nums)):
        currentSum+=nums[r]
        if (r-l+1)==k:
            average=currentSum/k
            maxSum=max(maxSum,average)
            minSum=min(minSum,average)
            currentSum-=nums[l]
            l+=1
    return maxSum-minSum
#time complexity O(n)
#space complexity O(1)