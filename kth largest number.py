class Solution:
    def kthLargestNumber(self, nums, k: int) -> str:
        nums = [int(i) for i in nums]
        nums.sort()
        n2 = nums[::-1]
        return str(n2[k-1])