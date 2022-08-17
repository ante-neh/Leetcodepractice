class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        l,r,counter=0,1,0
        while r<len(nums):
            if nums[l]!=nums[r]:
                counter=0
                l+=1
                nums[l]=nums[r]
            elif nums[l]==nums[r] and counter<0:
                counter+=1
                l+=1
                nums[l]=nums[r]
            r+=1
        return l+1
    #time complexity O(n)
    #space complexity O(1)