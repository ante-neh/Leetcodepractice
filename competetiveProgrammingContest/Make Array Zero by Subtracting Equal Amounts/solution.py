class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        visited=set()
        for r in range(len(nums)):
            if nums[r] not in visited and nums[r]!=0:
                visited.add(nums[r])
        return len(visited)