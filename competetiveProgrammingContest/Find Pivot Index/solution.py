class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum=0
        leftSum,rightSum=[],[]
        for i in range(len(nums)):
            sum+=nums[i]
            leftSum.append(sum)
        sum=0
        for num in reversed(nums):
            sum+=num
            rightSum.append(sum)
        for i in range(len(nums)):
            if leftSum[i]==rightSum[len(nums)-1-i]:
                return i
        return -1