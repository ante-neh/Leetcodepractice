class Solution:
    def numberOfGoodSegments(self,nums,s):
        l,sum=0,0
        maxSum=0
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>s:
                sum-=nums[l]
                l+=1
            maxSum+=r-l+1
        return maxSum