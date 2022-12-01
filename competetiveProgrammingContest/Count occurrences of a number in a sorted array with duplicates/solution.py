class Solution:
    def countOccurance(self, nums, target):
        firstPosition, lastPosition = -1, -1
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                firstPosition = m
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                lastPosition = m
                l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return lastPosition - firstPosition + 1