class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]*len(nums)
        left_sum=1
        right_sum=1
        l,r=0,len(nums)-1
        while l<len(nums) and r>=0:
            result[l]*=left_sum
            left_sum*=nums[l]
            result[r]*=right_sum
            right_sum*=nums[r]
            l,r=l+1,r-1
        return result
#time complexity O(n)
#space complexity O(n)