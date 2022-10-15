class Solution:
    def longestGoodSegment(self,nums,s):
        l,sum=0,0
        maxLen=0
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>s:
                sum-=nums[l]
                l+=1
            maxLen=max(maxLen,r-l+1)
        return maxLen