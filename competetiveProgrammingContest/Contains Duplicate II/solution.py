class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited=set()
        l,r=0,0
        while r<len(nums):
            if r-l>k:
                visited.remove(nums[l])
                l+=1
            if nums[r] not in visited:
                visited.add(nums[r])
            else:
                return True
            r+=1
        return False