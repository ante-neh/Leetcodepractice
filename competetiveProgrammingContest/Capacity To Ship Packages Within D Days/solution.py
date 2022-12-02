class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            D = 1
            total = 0 
            for weight in weights:
                total += weight
                if total > capacity:
                    total = weight
                    D += 1
                    if D > days:
                        return False
            return True
        
        l, r = max(weights), sum(weights)
        
        while l < r:
            m = l + (r - l) // 2
            if feasible(m):
                r = m
            else:
                l = m + 1
                
        return l