class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        leftsum=0
        for i,num in enumerate(nums):
            rightsum=total-num-leftsum
            if rightsum==leftsum:
                return i
            leftsum+=num
        return -1
#time complexity O(n)
#space complexity (1)