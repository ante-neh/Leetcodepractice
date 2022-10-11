class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l,r=0,len(nums)-1
        while l<r:
            if nums[l]%2==1:
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
            elif nums[l]%2==0:
                l+=1
        return nums