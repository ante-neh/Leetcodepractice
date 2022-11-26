class Solution:
    def leftBorderElement(self, nums, target):
        l, r = 0, len(nums) - 1
        leftBorder = -1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] < target:
                leftBorder = mid
                l = mid + 1
            else:
                r = mid - 1

        return leftBorder
