class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r=0,len(nums)-1
        counter=0
        while l<r:
            sum=nums[l]+nums[r]
            if sum<k:
                l+=1
            elif sum>k:
                r-=1
            else:
                counter+=1
                l+=1
                r-=1
        return counter