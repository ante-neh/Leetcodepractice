class Solution:
    def find_first_pos(self,nums, target):
        l, r = 0, len(nums) - 1
        firstPosition = -1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                firstPosition = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return firstPosition
