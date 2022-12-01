class Solution:
    def floarCeil(self, nums, target):
        l, r = 0, len(nums) - 1
        floar = -1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                floar = nums[m]
                break
            elif nums[m] < target:
                floar = nums[m]
                l = m + 1
            else:
                r = m - 1

        l, r = 0, len(nums) - 1
        ceil = -1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                ceil = nums[m]
                break
            elif nums[m] < target:
                l = m + 1
            else:
                ceil = nums[m]
                r = m - 1

        return [floar, ceil]