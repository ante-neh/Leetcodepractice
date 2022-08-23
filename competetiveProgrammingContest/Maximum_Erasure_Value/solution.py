class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        numsSet=set()
        l,sum=0,0
        maxScore=0
        for r in range(len(nums)):
            sum+=nums[r]
            while nums[r] in numsSet:
                sum-=nums[l]
                numsSet.remove(nums[l])
                l+=1
            numsSet.add(nums[r])
            maxScore=max(maxScore,sum)
        return maxScore
    #time complexity O(n)
    #space complexity O(1)