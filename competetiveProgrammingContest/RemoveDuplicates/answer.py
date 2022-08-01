class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        left,right,counter=0,1,0
        while right<len(nums):
            if (nums[left]!=nums[right]):
                left+=1
                nums[left]=nums[right]
                counter=0
            elif nums[left]==nums[right] and counter<1:
                counter+=1
                left+=1
                nums[left]=nums[right]
            right+=1
        return left+1         
    #time complexity O(n)
    #space complexity O(1)