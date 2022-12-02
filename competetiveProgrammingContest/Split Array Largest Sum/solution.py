class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(threshold):
            count, total = 1, 0
            
            for num in nums:
                total += num
                if total > threshold:
                    total = num
                    count += 1
                    if count > k:
                        return False
            
            return True
        
        l, r = max(nums), sum(nums)
        
        while l < r:
            m = l + (r - l) // 2
            if feasible(m):
                r = m
            else:
                l = m + 1
                
        return l