class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r=0,0
        maxPosFreq,sum=0,0
        while r<len(nums):
            sum+=nums[r]
            while nums[r]*(r-l+1)>sum+k:
                sum-=nums[l]
                l+=1
            maxPosFreq=max(maxPosFreq,r-l+1)
            r+=1
        return maxPosFreq
    #time complexity O(nlogn)
    #space complexity O(1)