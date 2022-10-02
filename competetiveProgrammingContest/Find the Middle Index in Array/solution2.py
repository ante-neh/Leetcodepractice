class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftSum,rightSum=[],[]
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            leftSum.append(sum)
        sum=0
        for num in reversed(nums):
            sum+=num
            rightSum.append(sum)
        for i in range(len(nums)):
            if leftSum[i]==rightSum[len(nums)-i-1]:
                return i
        return -1