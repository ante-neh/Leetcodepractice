class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        l, r = -1, -1
        count=0
        for i in range(len(nums)):
            if nums[i]>right:
                l = r = i
            elif nums[i]>=left:
                r=i
            count+=r-l
        return count