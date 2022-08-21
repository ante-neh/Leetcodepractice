def findMaxAverage(self, nums, k):
    currentSum=0
    maxAverage=-10000000000 #see the constraint part of the program is to get this value or you can use maxAverage=float("-inf")
    l=0
    for r in range(len(nums)):
        currentSum+=nums[r]
        if (r-l+1)==k:
            maxAverage=max(maxAverage,currentSum/k)
            currentSum-=nums[l]
            l+=1
    return maxAverage

#time complexity O(n)
#space complexity O(1)