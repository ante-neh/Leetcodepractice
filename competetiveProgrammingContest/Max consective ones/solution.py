class Solution:
    def findMaxConsecutiveOnes(self,nums:List[int])->int:
        l,maxLen=0,0
        for r in range(len(nums)):
            if nums[r]==0:
                l=r+1
            maxLen=max(maxLen,r-l+1)
        return maxLen