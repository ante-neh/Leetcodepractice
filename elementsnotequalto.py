class Solution:
    def rearrangeArray(self, nums):
        d = True
        while d:
            d = False
            i = len(nums)-2
            while i >= 0:
                if (nums[i+1] + nums[i-1]) / 2 == nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    d = True
                i -= 1
                
        return nums