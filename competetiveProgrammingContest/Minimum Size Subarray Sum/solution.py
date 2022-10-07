class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size,sum=float('inf'),0
        l=0
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>=target:
                size=min(r-l+1,size)
                sum-=nums[l]
                l+=1
        return size if size!=float('inf') else 0