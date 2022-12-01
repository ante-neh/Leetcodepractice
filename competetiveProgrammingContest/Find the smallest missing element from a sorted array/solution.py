class Solution:
    def minimumMissingNumber(self,nums):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2 
            if nums[m] == m:
                l = m + 1 
            else:
                r = m - 1
        
        return l