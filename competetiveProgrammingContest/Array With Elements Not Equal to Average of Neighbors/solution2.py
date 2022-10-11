class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if i%2==1 and nums[i]<nums[i-1]:
                nums[i],nums[i-1]=nums[i-1],nums[i]
            if i%2==0 and nums[i]>nums[i-1]:
                nums[i],nums[i-1]=nums[i-1],nums[i]
        return nums