class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxVal=0
        l,r=0,len(nums)-1
        while l<r:
            sum=nums[l]+nums[r]
            maxVal=max(maxVal,sum)
            l,r=l+1,r-1
        return maxVal