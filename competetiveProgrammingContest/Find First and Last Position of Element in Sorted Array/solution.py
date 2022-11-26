class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        firstPosition, lastPosition = -1, -1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                lastPosition = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        l, r = 0, len(nums) - 1 
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                firstPosition = mid
                r = mid - 1
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return [firstPosition, lastPosition]