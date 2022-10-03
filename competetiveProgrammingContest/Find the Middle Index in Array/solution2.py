class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftSum,rightSum=[],[]
        sum=0
        for num in nums:
            sum+=num
            leftSum.append(sum)
        sum=0
        for num in reversed(nums):
            sum+=num
            rightSum.append(sum)
        for i in range(len(nums)):
            if leftSum[i]==rightSum[len(nums)-1-i]:
                return i
        return -1