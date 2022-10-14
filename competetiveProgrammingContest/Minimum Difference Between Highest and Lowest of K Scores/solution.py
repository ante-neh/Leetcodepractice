class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minDiff=float('inf')
        l=0
        for r in range(len(nums)):
            if r-l+1==k:
                minDiff=min(minDiff,nums[r]-nums[l])
                l+=1
        return minDiff