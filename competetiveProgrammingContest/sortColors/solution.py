class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur,l,r=0,0,len(nums)-1
        while cur<=r:
            if nums[cur]==2:
                nums[cur],nums[r]=nums[r],nums[cur]
                r-=1
            elif nums[cur]==1:
                cur+=1
            else:
                nums[cur],nums[l]=nums[l],nums[cur]
                l+=1
                cur+=1
    #time complexity O(n)
    #space complexity O(1)