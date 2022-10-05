class NumArray:
    def __init__(self, nums: List[int]):
        self.prefsum=[0]
        for num in nums:
            self.prefsum.append(self.prefsum[-1]+num)
    def sumRange(self, left: int, right: int) -> int:
        return self.prefsum[right+1]-self.prefsum[left]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)