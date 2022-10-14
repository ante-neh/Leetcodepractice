class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        numsCount=set()
        l=0
        maxSum=0
        sum=0
        for r in range(len(nums)):
            sum+=nums[r]
            while nums[r] in numsCount:
                sum-=nums[l]
                numsCount.remove(nums[l])
                l+=1
            numsCount.add(nums[r])
            maxSum=max(maxSum,sum)
        return maxSum