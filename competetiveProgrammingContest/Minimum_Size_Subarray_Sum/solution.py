def minSubArrayLen(target, nums):
    l,minLen=0,float("inf")
    sum=0
    for r in range(len(nums)):
        sum+=nums[r]
        while sum>=target:
            minLen=min(minLen,r-l+1)
            sum-=nums[l]
            l+=1
    return minLen
#time complexity O(n)
#space complexity O(1)