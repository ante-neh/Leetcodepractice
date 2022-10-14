class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited=set()
        for r in range(len(nums)):
            if nums[r] not in visited:
                visited.add(nums[r])
            else:
                return True
        return False