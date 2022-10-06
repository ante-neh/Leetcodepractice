class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        prod=1
        counter=l=0
        for r in range(len(nums)):
            prod*=nums[r]
            while prod>=k:
                prod/=nums[l]
                l+=1
            counter+=r-l+1
        return counter