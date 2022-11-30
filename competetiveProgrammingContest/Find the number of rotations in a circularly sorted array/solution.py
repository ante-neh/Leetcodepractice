class Solution:
    def findRotationCount(self,nums):
        if len(nums) == 1:
            return 0
        
        l, r = 0, len(nums) - 1

        if nums[r] > nums[0]:
            return 0

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > nums[m + 1]:
                return m + 1
            elif nums[m] < nums[m - 1]:
                return m
            if nums[m] > nums[0]:
                l = m + 1
            else:
                r = m - 1