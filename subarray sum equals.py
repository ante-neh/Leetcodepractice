class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, preSum, cnt = collections.defaultdict(int), 0, 0
        count[0] = 1
        for num in nums:
            preSum += num
            if count[preSum - k]:
                cnt += count[preSum - k]
            count[preSum] += 1
        return cnt