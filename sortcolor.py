class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            min=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[min]:
                    min=j               
            if min!=i:
                nums[i],nums[min]=nums[min],nums[i]
        return nums