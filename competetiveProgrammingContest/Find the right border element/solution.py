class Solution:
    def rightBorderElement(self, nums, target):
        l, r = 0, len(nums) - 1
        rightBorder = -1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] <= target:
                l = mid + 1
            else:
                rightBorder = mid
                r = mid -1
        return rightBorder