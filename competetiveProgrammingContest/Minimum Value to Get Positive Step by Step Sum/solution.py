class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            nums[i]=sum
        minSum=min(nums)
        if minSum<0:
            return abs(minSum)+1
        else:
            return 1
            