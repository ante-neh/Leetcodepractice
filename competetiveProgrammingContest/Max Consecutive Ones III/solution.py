class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        counter,l=0,0
        maxLen=0
        for r in range(len(nums)):
            if nums[r]==0:
                counter+=1
            while counter>k:
                if nums[l]==0:
                    counter-=1
                l+=1
            maxLen=max(maxLen,r-l+1)
        return maxLen