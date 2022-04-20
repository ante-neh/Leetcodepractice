class Solution:
    def minPairSum(self, nums) -> int:
        nums.sort()
        ma = nums[0] + nums[1]
        l, h = 0, len(nums) - 1

        while(l < h):
            if nums[l] + nums[h] > ma:
                ma = nums[l] + nums[h]
            l, h  = l + 1, h - 1

        return ma