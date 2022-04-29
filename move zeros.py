class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in reversed(range(len(nums))):
            if nums[i]==0:
                del nums[i]
                i-=1
                nums+=[0]
        return nums