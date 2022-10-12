class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nums.sort()
        even,odd=0,1
        while even<len(nums) and odd<len(nums):
            if nums[even]%2==0:
                even+=2
            else:
                nums[odd],nums[even]=nums[even],nums[odd]
                odd+=2
        return nums