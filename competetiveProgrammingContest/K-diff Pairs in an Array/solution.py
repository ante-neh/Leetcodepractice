class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        count = 0
        for r in range(1,len(nums)):
            if r + 1 < len(nums) and nums[r] == nums[r+1]:
                continue
            while l > 0 and nums[l] == nums[l-1]:
                l += 1
            while nums[r] - nums[l] > k and l + 1 < r:
                l+=1
            if nums[r] - nums[l] == k:
                count += 1
        return count