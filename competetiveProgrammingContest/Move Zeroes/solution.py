class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 1
        
        while l < len(nums) and r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
            if nums[l] != 0:
                l += 1
            if nums[r] == 0 or r <= l:
                r += 1