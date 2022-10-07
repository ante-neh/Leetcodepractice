class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefix_sum = 0
        cache = []
        for i, v in enumerate(chalk):
            prefix_sum += v
            cache.append(prefix_sum)
        
        n = k // prefix_sum
        k -= prefix_sum * n
        # binary search the residul, find the first index that is larger than residul
        return bisect.bisect_right(cache, k)
        