class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum=0
        mindiff=float("inf")
        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            while l<r:
                threesum=nums[i]+nums[l]+nums[r]
                if threesum==target:
                    return threesum
                elif threesum<target:
                    l+=1
                else:
                    r-=1
                curdiff=abs(target-threesum)
                if curdiff<mindiff:
                    mindiff=curdiff
                    result=threesum
        return result
    #time complexity O(nlogn)
    #space complexity O(1)