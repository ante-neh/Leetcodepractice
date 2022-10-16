class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r=0,1
        while r<len(nums) and l<len(nums):
            if nums[r]!=nums[r-1]:
                l+=1
                nums[l]=nums[r]
            r+=1
        return l+1