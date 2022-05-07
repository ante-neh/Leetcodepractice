class Solution:
    def minIncrementForUnique(self, nums) -> int:
        nums.sort()
        minIncrement = 0
        for i in range(1,len(nums)):
            if nums[i-1] >= nums[i]: 
                minIncrement += nums[i-1]-nums[i]+1
                nums[i] = nums[i-1]+1
        return minIncrement