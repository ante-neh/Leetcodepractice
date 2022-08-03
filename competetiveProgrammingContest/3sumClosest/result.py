class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result=0
        minDiff=10001
        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            while l<r:
                threesum=nums[i]+nums[l]+nums[r]
                if threesum<target:
                    l+=1
                elif threesum>target:
                    r-=1
                else:
                    return threesum
            curDiff=abs(threesum-target)
            if curDiff<minDiff:
                minDiff=curDiff
                result=threesum
        return result
    #time complexity O(nlogn)
    #space complexity O(1)